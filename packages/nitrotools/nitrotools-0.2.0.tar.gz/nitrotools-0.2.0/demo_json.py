#!/usr/bin/env python3
"""
Demo script for the new generate_json functionality in nitrotools.

This script demonstrates how to use the generate_json method to get
structured JSON responses from LLMs with automatic JSON repair.

Usage:
    export OPENROUTER_API_KEY="your_key_here"
    python demo_json.py
"""

import os
import json
from nitro import get_llm

def demo_quiz_generation():
    """Demo: Generate a quiz in JSON format."""
    print("🎯 Demo: Generating a quiz on current Indian affairs")
    print("=" * 60)

    # Get LLM instance (using OpenRouter for demo)
    llm = get_llm("reasoning")

    # Example prompt for quiz generation
    prompt = """Create a quiz of 5 questions on current Indian affairs.
Each question should have:
- question: the question text
- options: array of 4 possible answers
- correct_option: index (0-3) of the correct answer

Return as a JSON array of question objects."""

    try:
        quiz_data = llm.generate_json(prompt)
        print("✅ Successfully generated quiz JSON:")
        print(json.dumps(quiz_data, indent=2))

        # Validate structure
        assert isinstance(quiz_data, list), "Expected list of questions"
        assert len(quiz_data) == 5, "Expected 5 questions"
        for i, q in enumerate(quiz_data):
            assert "question" in q, f"Question {i} missing 'question' field"
            assert "options" in q, f"Question {i} missing 'options' field"
            assert "correct_option" in q, f"Question {i} missing 'correct_option' field"
            assert isinstance(q["options"], list), f"Question {i} options should be list"
            assert len(q["options"]) == 4, f"Question {i} should have 4 options"
            assert isinstance(q["correct_option"], int), f"Question {i} correct_option should be int"
            assert 0 <= q["correct_option"] <= 3, f"Question {i} correct_option should be 0-3"

        print("✅ JSON structure validation passed!")

    except Exception as e:
        print(f"❌ Error generating quiz: {e}")

def demo_person_profile():
    """Demo: Generate a person profile with schema."""
    print("\n👤 Demo: Generating a person profile with schema")
    print("=" * 60)

    llm = get_llm("analysis")

    prompt = "Generate a profile for a fictional software engineer."

    # Optional: Define a JSON schema
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer", "minimum": 18, "maximum": 80},
            "skills": {"type": "array", "items": {"type": "string"}},
            "experience_years": {"type": "integer"},
            "current_company": {"type": "string"}
        },
        "required": ["name", "age", "skills"]
    }

    try:
        profile = llm.generate_json(prompt, json_schema=schema)
        print("✅ Successfully generated profile JSON:")
        print(json.dumps(profile, indent=2))

        # Basic validation
        assert isinstance(profile, dict), "Expected object"
        assert "name" in profile, "Missing required field: name"
        assert "age" in profile, "Missing required field: age"
        assert "skills" in profile, "Missing required field: skills"

        print("✅ JSON structure validation passed!")

    except Exception as e:
        print(f"❌ Error generating profile: {e}")

def demo_custom_role():
    """Demo: Using custom role parameter."""
    print("\n🎭 Demo: Using custom role parameter")
    print("=" * 60)

    llm = get_llm("assistant")

    # Using system role for context
    system_prompt = """You are a helpful assistant that generates JSON data.
Always respond with valid JSON only."""

    prompt = """Generate a simple todo list with 3 items.
Format: {"todos": [{"task": "string", "priority": "high|medium|low"}]}"""

    try:
        # Note: generate_json uses the role parameter for the message
        todo_data = llm.generate_json(prompt, role="user")
        print("✅ Successfully generated todo JSON:")
        print(json.dumps(todo_data, indent=2))

    except Exception as e:
        print(f"❌ Error generating todo: {e}")

def main():
    """Run all demos."""
    print("🚀 NitroTools JSON Generation Demo")
    print("=" * 60)

    # Check for required environment variables
    if not os.getenv('OPENROUTER_API_KEY'):
        print("❌ OPENROUTER_API_KEY environment variable not set!")
        print("Please set it with: export OPENROUTER_API_KEY='your_key_here'")
        return

    try:
        # Run demos
        demo_quiz_generation()
        demo_person_profile()
        demo_custom_role()

        print("\n🎉 All demos completed successfully!")
        print("\n💡 Tips:")
        print("- The generate_json method automatically repairs malformed JSON")
        print("- Use json_schema parameter to guide the LLM toward specific structures")
        print("- The method works with any OpenAI-compatible LLM (OpenRouter, LlamaCPP)")

    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Install with: pip install nitrotools[llm]")

if __name__ == "__main__":
    main()
