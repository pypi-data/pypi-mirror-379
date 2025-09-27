import pytest
import os
from nitro import get_llm, LLMFactory


class TestLLMIntegration:
    """Integration tests with real LLM calls (requires credentials)."""

    @pytest.mark.skipif(not os.getenv("OPENROUTER_API_KEY"), reason="OPENROUTER_API_KEY not set")
    def test_real_openrouter_generate(self):
        """Test real generate call with OpenRouter."""
        llm = get_llm("assistant")  # Assuming mapped to openrouter
        messages = [{"role": "user", "content": "Say hello in one word."}]
        response = llm.generate(messages)
        print(f"OpenRouter generate response: {response}")
        assert isinstance(response, str)
        assert len(response.strip()) > 0

    @pytest.mark.skipif(not os.getenv("OPENROUTER_API_KEY"), reason="OPENROUTER_API_KEY not set")
    def test_real_openrouter_chat(self):
        """Test real chat call with OpenRouter."""
        llm = get_llm("assistant")
        messages = [{"role": "user", "content": "What is 2+2?"}]
        response = llm.chat(messages)
        print(f"OpenRouter chat response: {response}")
        # response is raw dict/object, check it has expected keys
        assert hasattr(response, 'choices') or isinstance(response, dict)

    @pytest.mark.skipif(not os.getenv("LLAMACPP_BASE_URL"), reason="LLAMACPP_BASE_URL not set")
    def test_real_llamacpp_generate_openai_compatible(self):
        """Test real generate call with LlamaCPP using OpenAI compatible interface."""
        llm = get_llm("general")  # Assuming mapped to llamacpp
        messages = [{"role": "user", "content": "Hello"}]
        response = llm.generate(messages)
        print(f"LlamaCPP OpenAI compatible generate response: {response}")
        assert isinstance(response, str)

    @pytest.mark.skipif(not os.getenv("LLAMACPP_BASE_URL"), reason="LLAMACPP_BASE_URL not set")
    def test_real_llamacpp_chat_openai_compatible(self):
        """Test real chat call with LlamaCPP using OpenAI compatible interface."""
        llm = get_llm("general")
        messages = [{"role": "user", "content": "What is the capital of France?"}]
        response = llm.chat(messages)
        print(f"LlamaCPP OpenAI compatible chat response: {response}")
        assert hasattr(response, 'choices') or isinstance(response, dict)

    @pytest.mark.skipif(not os.getenv("LLAMACPP_BASE_URL"), reason="LLAMACPP_BASE_URL not set")
    def test_real_llamacpp_generate_langchain(self):
        """Test real generate call with LlamaCPP using LangChain interface."""
        # Set dummy API key for LangChain
        original_api_key = os.environ.get("OPENAI_API_KEY")
        os.environ["OPENAI_API_KEY"] = "dummy"
        try:
            factory = LLMFactory()
            # Temporarily change interface to langchain
            original_servers = factory.servers.copy()
            factory.servers["llamacpp"][0]["interface"] = "langchain"
            try:
                llm = factory.get_llm("general")
                messages = [{"role": "user", "content": "Hello"}]
                response = llm.generate(messages)
                print(f"LlamaCPP LangChain generate response: {response}")
                assert isinstance(response, str)
            finally:
                factory.servers = original_servers
        finally:
            if original_api_key is not None:
                os.environ["OPENAI_API_KEY"] = original_api_key
            else:
                os.environ.pop("OPENAI_API_KEY", None)

    @pytest.mark.skipif(not os.getenv("LLAMACPP_BASE_URL"), reason="LLAMACPP_BASE_URL not set")
    def test_real_llamacpp_chat_langchain(self):
        """Test real chat call with LlamaCPP using LangChain interface."""
        # Set dummy API key for LangChain
        original_api_key = os.environ.get("OPENAI_API_KEY")
        os.environ["OPENAI_API_KEY"] = "dummy"
        try:
            factory = LLMFactory()
            # Temporarily change interface to langchain
            original_servers = factory.servers.copy()
            factory.servers["llamacpp"][0]["interface"] = "langchain"
            try:
                llm = factory.get_llm("general")
                messages = [{"role": "user", "content": "What is the capital of France?"}]
                response = llm.chat(messages)
                print(f"LlamaCPP LangChain chat response: {response}")
                # LangChain response is AIMessage object
                assert hasattr(response, 'content')
            finally:
                factory.servers = original_servers
        finally:
            if original_api_key is not None:
                os.environ["OPENAI_API_KEY"] = original_api_key
            else:
                os.environ.pop("OPENAI_API_KEY", None)

    @pytest.mark.skipif(not os.getenv("OPENROUTER_API_KEY"), reason="OPENROUTER_API_KEY not set")
    def test_generate_json_openrouter(self):
        """Test generate_json method with OpenRouter."""
        try:
            import json_repair
        except ImportError:
            pytest.skip("json-repair package not installed")

        llm = get_llm("reasoning")  # Should be OpenRouter grok-fast-free

        # Test with a simple JSON generation prompt
        prompt = """Generate a JSON object for a person with the following fields:
- name: string
- age: number
- city: string"""

        result = llm.generate_json(prompt)

        assert isinstance(result, dict)
        assert "name" in result
        assert isinstance(result["age"], (int, float))
        assert "city" in result

        print(f"Generated JSON: {result}")


if __name__ == "__main__":
    pytest.main([__file__])
