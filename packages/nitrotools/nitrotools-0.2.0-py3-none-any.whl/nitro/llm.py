"""Lean LLM Factory for Multi-Server Language Model Support with Protocol-Based Interfaces

Simple, focused LLM factory with predefined configurations for different purposes.
Supports multiple providers and interfaces via a unified protocol.
"""

import json
import os
from typing import Dict, List, Any, Optional, TypedDict, runtime_checkable, TYPE_CHECKING

import yaml
from dotenv import load_dotenv

from .logging import get_logger

# Optional imports
if TYPE_CHECKING:
    import openai
    from langchain_openai import ChatOpenAI
else:
    try:
        import openai
    except ImportError:
        openai = None

    try:
        from langchain_openai import ChatOpenAI
    except ImportError:
        ChatOpenAI = None

    try:
        import json_repair
    except ImportError:
        json_repair = None

# Type definitions for config
class ModelConfig(TypedDict, total=False):
    name: str
    model: Optional[str]
    model_name: Optional[str]
    temperature: float
    max_tokens: int

class LlamaCPPServerConfig(TypedDict):
    endpoint: str
    interface: str
    models: List[ModelConfig]

class OpenRouterServerConfig(TypedDict):
    endpoint: str
    api_key: str
    interface: str
    headers: Dict[str, str]
    models: List[ModelConfig]

class ConfigData(TypedDict):
    servers: Dict[str, Any]  # LlamaCPP: List[LlamaCPPServerConfig], OpenRouter: OpenRouterServerConfig
    purposes: Dict[str, str]

load_dotenv()
logger = get_logger(__name__)

# Protocol for LLM Interfaces
from typing import Protocol

from typing import runtime_checkable

@runtime_checkable
class BaseLLM(Protocol):
    """Protocol for LLM interfaces. Implementations must provide these methods."""

    def generate(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """
        Generate a text response from messages.

        Args:
            messages: List of message dicts (e.g., [{"role": "user", "content": "..."}]).
            **kwargs: Optional params like temperature, max_tokens.

        Returns:
            str: The generated text response.
        """
        ...

    def chat(self, messages: List[Dict[str, str]], **kwargs) -> Any:
        """
        Generate a full chat response.

        Args:
            messages: Same as generate.
            **kwargs: Same as generate.

        Returns:
            Any: The full raw response from the backend.
        """
        ...

    @property
    def provider(self) -> str:
        """Return the provider name (e.g., 'llamacpp', 'openrouter')."""
        ...

    @property
    def model(self) -> str:
        """Return the model name (e.g., 'qwen', 'gpt-4o-mini')."""
        ...

# Implementations

class LangChainLLM:
    """LangChain-based LLM implementation."""

    def __init__(self, model: Any, provider: str, model_name: str):
        self._model = model
        self._provider = provider
        self._model_name = model_name

    def generate(self, messages: List[Dict[str, str]], **kwargs) -> str:
        from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
        lc_messages: List[BaseMessage] = []
        for msg in messages:
            if msg["role"] == "user":
                lc_messages.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "assistant":
                lc_messages.append(AIMessage(content=msg["content"]))
        response = self._model.invoke(lc_messages, **kwargs)
        return response.content

    def chat(self, messages: List[Dict[str, str]], **kwargs) -> Any:
        from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
        lc_messages: List[BaseMessage] = []
        for msg in messages:
            if msg["role"] == "user":
                lc_messages.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "assistant":
                lc_messages.append(AIMessage(content=msg["content"]))
        return self._model.invoke(lc_messages, **kwargs)

    @property
    def provider(self) -> str:
        return self._provider

    @property
    def model(self) -> str:
        return self._model_name

class OpenAICompatibleLLM:
    """OpenAI-compatible LLM implementation (e.g., for OpenRouter)."""

    def __init__(self, client: Any, provider: str, model_name: str, headers: Optional[Dict[str, str]] = None):
        self._client = client
        self._provider = provider
        self._model_name = model_name
        self._headers = headers or {}

    @classmethod
    def from_config(cls, base_url: str, api_key: str, model_name: str, provider: str, headers: Optional[Dict[str, str]] = None):
        if openai is None:
            raise ImportError("openai package is required for OpenAICompatibleLLM")
        client = openai.Client(base_url=base_url, api_key=api_key, default_headers=headers or {})
        return cls(client, provider, model_name, headers)

    def generate(self, messages: List[Dict[str, str]], **kwargs) -> str:
        response = self._client.chat.completions.create(
            model=self._model_name,
            messages=messages,
            **kwargs
        )
        return response.choices[0].message.content

    def chat(self, messages: List[Dict[str, str]], **kwargs) -> Any:
        return self._client.chat.completions.create(
            model=self._model_name,
            messages=messages,
            **kwargs
        )

    @property
    def provider(self) -> str:
        return self._provider

    @property
    def model(self) -> str:
        return self._model_name

    def generate_json(self, prompt: str, role: str = "user", json_schema: Optional[Dict[str, Any]] = None, **kwargs) -> Any:
        """
        Generate a JSON response from a prompt, with automatic JSON repair.

        This method standardizes the prompt to ensure valid JSON output and uses
        json-repair to handle any formatting issues in the LLM response.

        Args:
            prompt (str): The main prompt describing what JSON to generate.
            role (str): The role for the message (default: "user").
            json_schema (Optional[Dict]): Optional JSON schema to guide the response.
            **kwargs: Additional parameters for the chat completion.

        Returns:
            Any: The repaired JSON object.

        Raises:
            ImportError: If json-repair package is not installed.
            ValueError: If JSON repair fails.
        """
        if json_repair is None:
            raise ImportError("json-repair package is required for generate_json. Install with: pip install json-repair")

        # Standardize the prompt for better JSON generation
        standardized_prompt = self._standardize_json_prompt(prompt, json_schema)

        # Create messages
        messages = [{"role": role, "content": standardized_prompt}]

        # Get response
        response = self.chat(messages, **kwargs)
        content = response.choices[0].message.content

        # Repair and parse JSON
        try:
            repaired_json = json_repair.loads(content)
            return repaired_json
        except Exception as e:
            raise ValueError(f"Failed to repair JSON from response: {e}. Raw content: {content}")

    def _standardize_json_prompt(self, prompt: str, json_schema: Optional[Dict[str, Any]] = None) -> str:
        """
        Standardize the prompt to ensure consistent JSON generation.

        Args:
            prompt (str): Original prompt.
            json_schema (Optional[Dict]): JSON schema if provided.

        Returns:
            str: Standardized prompt.
        """
        standardized = f"""You are a JSON generation assistant. Your task is to generate valid JSON based on the following request.

{prompt}

IMPORTANT INSTRUCTIONS:
1. Return ONLY valid JSON - no markdown, no explanations, no code blocks.
2. Ensure the JSON is properly formatted and parseable.
3. Do not include any text before or after the JSON.
4. If the request asks for an array, return a JSON array.
5. If the request asks for an object, return a JSON object."""

        if json_schema:
            import json
            schema_str = json.dumps(json_schema, indent=2)
            standardized += f"""

JSON SCHEMA TO FOLLOW:
{schema_str}

Ensure your response matches this schema structure."""

        standardized += "\n\nGenerate the JSON now:"
        return standardized

class LLMFactory:
    """Lean factory for LLM instances with predefined configurations."""

    def __init__(self):
        self._llm_cache: Dict[str, BaseLLM] = {}
        self.default_interface: str
        self.llm_config: Dict[str, str]
        self.servers: Dict[str, Any]
        self._load_config()

    def _substitute_env_vars(self, data: Any) -> Any:
        """Recursively substitute ${VAR} with environment variables in data."""
        if isinstance(data, dict):
            return {k: self._substitute_env_vars(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [self._substitute_env_vars(item) for item in data]
        elif isinstance(data, str):
            return os.path.expandvars(data)
        else:
            return data

    def _load_config(self) -> None:
        """Load LLM configurations from YAML file or defaults."""

        # Default interface
        self.default_interface = os.getenv("DEFAULT_INTERFACE", "langchain")

        # Default configurations
        default_servers: Dict[str, Any] = {
            "llamacpp": [
                {
                    "endpoint": "http://10.2.0.5:11435",
                    "interface": "openai_compatible",
                    "models": [
                        {
                            "name": "qwen",
                            "model_name": "gpt-oss-20b-Q6_K.gguf",
                            "temperature": 0.7,
                            "max_tokens": 1000
                        },
                        {
                            "name": "deepseek",
                            "model_name": "deepseek-coder.gguf",
                            "temperature": 0.1,
                            "max_tokens": 1500
                        }
                    ],
                }
            ],
            "openrouter": {
                "endpoint": "https://openrouter.ai/api/v1",
                "api_key": os.getenv("OPENROUTER_API_KEY", ""),
                "interface": "openai_compatible",
                "headers": {
                    "HTTP-Referer": os.getenv("OPENROUTER_HTTP_REFERER", ""),
                    "X-Title": os.getenv("OPENROUTER_X_TITLE", "")
                },
                "models": [
                    {
                        "name": "gpt-4o-mini",
                        "model": "openai/gpt-4o-mini",
                        "temperature": 0.3,
                        "max_tokens": 1000,
                    },
                    {
                        "name": "deepseek-coder",
                        "model": "deepseek/deepseek-coder",
                        "temperature": 0.1,
                        "max_tokens": 1500,
                    }
                ],
            },
        }

        default_purposes: Dict[str, str] = {
            "general": "llamacpp:qwen",
            "coding": "llamacpp:qwen",
            "reasoning": "llamacpp:qwen",
            "analysis": "llamacpp:qwen",
            "route": "llamacpp:qwen",
            "retrieval": "llamacpp:qwen",
            "assistant": "llamacpp:qwen",
            "assistant_coding": "llamacpp:qwen",
            "assistant_reasoning": "llamacpp:qwen",
        }

        # Load from YAML if specified
        config_path = os.getenv("NITRO_CONFIG_PATH", "llm_config.yaml")
        if os.path.isfile(config_path):
            try:
                with open(config_path, 'r') as f:
                    config: ConfigData = yaml.safe_load(f)
                config = self._substitute_env_vars(config)
                self.servers = config.get("servers", default_servers)
                self.llm_config = config.get("purposes", default_purposes)
                logger.info(f"Loaded config from {config_path}")
            except Exception as e:
                logger.warning(f"Failed to load config from {config_path}: {e}. Using defaults.")
                self.servers = default_servers
                self.llm_config = default_purposes
        else:
            logger.warning(f"Config file {config_path} not found. Please copy nitro/llm_config.yaml.sample to {config_path} and configure it. Using defaults.")
            self.servers = default_servers
            self.llm_config = default_purposes

        # Allow override from environment
        config_override = os.getenv("LLM_CONFIG")
        if config_override:
            try:
                override_config = json.loads(config_override)
                if isinstance(override_config, dict):
                    self.llm_config.update(override_config)
                    logger.info("Loaded LLM config override from environment")
                else:
                    logger.warning(f"LLM_CONFIG is not a dict: {type(override_config)}. Using defaults.")
            except json.JSONDecodeError as e:
                logger.warning(f"Invalid LLM_CONFIG JSON: {e}. Using defaults.")

    def get_llm(self, purpose_or_node: str = "general") -> BaseLLM:
        """
        Get LLM for purpose or node name.

        Args:
            purpose_or_node: Purpose ("general", "coding") or node name ("assistant", "route")

        Returns:
            BaseLLM: Configured LLM instance
        """
        # Get provider:model from config
        provider_model: str = self.llm_config.get(
            purpose_or_node, self.llm_config["general"]
        )
        provider, model = provider_model.split(":", 1)

        cache_key = f"{provider}:{model}:{self._get_interface_for_provider(provider, model)}"

        # Return cached instance
        if cache_key in self._llm_cache:
            return self._llm_cache[cache_key]

        logger.info(f"🏭 Creating LLM for '{purpose_or_node}': {provider}/{model}")

        try:
            if provider == "llamacpp":
                llm = self._create_llamacpp_llm(model)
            elif provider == "openrouter":
                llm = self._create_openrouter_llm(model)
            else:
                raise ValueError(f"Unknown provider: {provider}")

            self._llm_cache[cache_key] = llm
            logger.info(f"✅ Created {provider}/{model} for '{purpose_or_node}'")
            return llm

        except Exception as e:
            logger.error(f"❌ Failed to create LLM for '{purpose_or_node}': {e}")
            # Fallback to general if not already trying general
            if purpose_or_node != "general":
                logger.info("🔄 Falling back to general LLM")
                return self.get_llm("general")
            raise

    def _get_interface_for_provider(self, provider: str, model: str) -> str:
        """Get the interface for a provider and model."""
        if provider == "llamacpp":
            # Find the server that has the model
            servers: List[LlamaCPPServerConfig] = self.servers[provider]
            for server in servers:
                if any(m["name"] == model for m in server["models"]):
                    return server["interface"]
            return self.default_interface
        elif provider == "openrouter":
            server_config: OpenRouterServerConfig = self.servers[provider]
            return server_config["interface"]
        return self.default_interface

    def _create_llamacpp_llm(self, model: str) -> BaseLLM:
        """Create LlamaCPP LLM instance."""
        # Find the server and model config
        servers: List[LlamaCPPServerConfig] = self.servers["llamacpp"]
        for server in servers:
            for m in server["models"]:
                if m["name"] == model:
                    interface = server["interface"]
                    actual_model_name = m.get("model_name", model)

                    if interface == "langchain":
                        if ChatOpenAI is None:
                            raise ImportError("langchain-openai package is required for langchain interface")
                        llm = ChatOpenAI(
                            base_url=f"{server['endpoint']}/v1",
                            api_key=None,
                            model=actual_model_name or model,
                            temperature=m["temperature"],
                        )
                        return LangChainLLM(llm, "llamacpp", model)
                    elif interface == "openai_compatible":
                        return OpenAICompatibleLLM.from_config(
                            base_url=f"{server['endpoint']}/v1",
                            api_key="not-needed-for-local",
                            model_name=actual_model_name or model,
                            provider="llamacpp"
                        )
                    else:
                        raise ValueError(f"Unsupported interface for llamacpp: {interface}")
        raise ValueError(f"No server found for model '{model}' in llamacpp")

    def _create_openrouter_llm(self, model: str) -> BaseLLM:
        """Create OpenRouter LLM instance."""
        server_config: OpenRouterServerConfig = self.servers["openrouter"]
        interface = server_config["interface"]
        api_key = server_config["api_key"]
        headers = server_config.get("headers", {})

        if not api_key:
            raise ValueError("OPENROUTER_API_KEY environment variable required")

        # Find model config
        model_config: Optional[ModelConfig] = None
        for m in server_config["models"]:
            if m["name"] == model:
                model_config = m
                break
        if not model_config:
            model_config = server_config["models"][0]  # Default to first

        actual_model = model_config.get("model") or model

        if interface == "openai_compatible":
            return OpenAICompatibleLLM.from_config(
                base_url=server_config["endpoint"],
                api_key=api_key,
                model_name=actual_model,
                provider="openrouter",
                headers=headers
            )
        else:
            raise ValueError(f"Unsupported interface for openrouter: {interface}")

    def health_check(self) -> Dict[str, str]:
        """Quick health check of configured providers."""
        status: Dict[str, str] = {}

        # Check each configured provider:model
        for purpose, provider_model in self.llm_config.items():
            try:
                llm = self.get_llm(purpose)
                status[purpose] = f"✅ {provider_model}"
            except Exception as e:
                status[purpose] = f"❌ {provider_model} ({str(e)[:50]}...)"

        return status

# Global factory instance
llm_factory = LLMFactory()

def get_llm(purpose_or_node: str = "general") -> BaseLLM:
    """Convenience function to get LLM."""
    return llm_factory.get_llm(purpose_or_node)
