#!/usr/bin/env python3
"""
Performance comparison script for all configured LLM purposes.

This script tests response time, token usage, and basic functionality
for each purpose defined in llm_config.yaml.

Usage:
    export OPENROUTER_API_KEY="your_key_here"
    python performance_test.py
"""

import time
import os
from nitro import get_llm, LLMFactory

def test_llm_performance(purpose, query="Explain the concept of recursion in programming."):
    """
    Test a single LLM purpose with timing and token metrics.

    Args:
        purpose (str): The purpose name from config
        query (str): Test query to run

    Returns:
        dict: Performance metrics
    """
    try:
        start_time = time.time()
        llm = get_llm(purpose)

        # Test chat method
        response = llm.chat([{"role": "user", "content": query}])

        end_time = time.time()
        latency = end_time - start_time

        # Extract metrics
        usage = response.usage
        content_length = len(response.choices[0].message.content)

        return {
            'purpose': purpose,
            'success': True,
            'latency_seconds': round(latency, 2),
            'prompt_tokens': usage.prompt_tokens,
            'completion_tokens': usage.completion_tokens,
            'total_tokens': usage.total_tokens,
            'content_length_chars': content_length,
            'model': response.model,
            'error': None
        }

    except Exception as e:
        return {
            'purpose': purpose,
            'success': False,
            'latency_seconds': None,
            'prompt_tokens': None,
            'completion_tokens': None,
            'total_tokens': None,
            'content_length_chars': None,
            'model': None,
            'error': str(e)
        }

def main():
    """Run performance tests for all configured purposes."""

    # Check for required environment variables
    if not os.getenv('OPENROUTER_API_KEY'):
        print("⚠️  Warning: OPENROUTER_API_KEY not set. OpenRouter tests will fail.")

    # Get all configured purposes
    factory = LLMFactory()
    purposes = list(factory.llm_config.keys())

    if not purposes:
        print("❌ No purposes found in config")
        return

    print(f"🚀 Testing {len(purposes)} LLM purposes...")
    print("=" * 80)

    results = []
    for purpose in purposes:
        print(f"Testing '{purpose}'...")
        result = test_llm_performance(purpose)
        results.append(result)

        if result['success']:
            print(f"  ✅ Success - {result['latency_seconds']}s, {result['total_tokens']} tokens")
        else:
            print(f"  ❌ Failed - {result['error']}")

    print("\n" + "=" * 80)
    print("📊 PERFORMANCE RESULTS")
    print("=" * 80)

    # Print summary table
    print(f"{'Purpose':<20} {'Success':<8} {'Latency(s)':<10} {'Tokens':<8} {'Chars':<8} {'Model'}")
    print("-" * 80)

    for result in results:
        success = "✅" if result['success'] else "❌"
        latency = f"{result['latency_seconds']}" if result['latency_seconds'] else "N/A"
        tokens = f"{result['total_tokens']}" if result['total_tokens'] else "N/A"
        chars = f"{result['content_length_chars']}" if result['content_length_chars'] else "N/A"
        model = result['model'] or "N/A"

        print(f"{result['purpose']:<20} {success:<8} {latency:<10} {tokens:<8} {chars:<8} {model}")

    # Summary stats
    successful = [r for r in results if r['success']]
    if successful:
        avg_latency = sum(r['latency_seconds'] for r in successful) / len(successful)
        total_tokens = sum(r['total_tokens'] for r in successful)
        print(f"\n📈 Summary: {len(successful)}/{len(results)} successful")
        print(f"   Average latency: {avg_latency:.2f}s")
        print(f"   Total tokens used: {total_tokens}")
    else:
        print("\n❌ All tests failed")

if __name__ == "__main__":
    main()
