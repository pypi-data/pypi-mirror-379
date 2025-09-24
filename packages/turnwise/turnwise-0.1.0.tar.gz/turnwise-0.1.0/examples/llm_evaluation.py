#!/usr/bin/env python3
"""Example demonstrating LLM-based evaluation with Turnwise."""

import os

from turnwise import (
    Conversation,
    ConversationQualityMetric,
    Evaluator,
    ResponseHelpfulnessMetric,
    ResponseSafetyMetric,
    Role,
    Turn,
)


def main():
    print("=== Turnwise LLM Evaluation Example ===\n")

    # Check if API key is available
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  OPENAI_API_KEY environment variable not set!")
        print("   Set it to use LLM-based metrics:")
        print("   export OPENAI_API_KEY='your-api-key-here'")
        print()
        return

    # Create a sample conversation
    conversation = Conversation(
        turns=[
            Turn(
                role=Role.USER,
                content="I'm having trouble with my Python code. Can you help?",
            ),
            Turn(
                role=Role.ASSISTANT,
                content="Of course! I'd be happy to help you with your Python code. Could you please share the specific error message you're seeing, or describe what you're trying to accomplish? The more details you provide, the better I can assist you.",
            ),
            Turn(
                role=Role.USER,
                content="I'm getting a 'list index out of range' error when trying to access the first element of a list.",
            ),
            Turn(
                role=Role.ASSISTANT,
                content="A 'list index out of range' error typically occurs when you're trying to access an index that doesn't exist in the list. Here are the most common causes and solutions:\n\n1. **Empty list**: If your list is empty, accessing index 0 will cause this error.\n2. **Wrong index**: Make sure you're using the correct index (remember Python uses 0-based indexing).\n3. **Dynamic list changes**: If you're modifying the list while iterating, indices might change.\n\nCould you share the specific code that's causing the error? That way I can give you a more targeted solution.",
            ),
            Turn(
                role=Role.USER,
                content="Thanks! That makes sense. I think my list is empty when I try to access it.",
            ),
            Turn(
                role=Role.ASSISTANT,
                content="Perfect! That's a very common issue. Here are a few ways to handle empty lists safely:\n\n```python\n# Method 1: Check if list is not empty\nif my_list:\n    first_item = my_list[0]\nelse:\n    print('List is empty')\n\n# Method 2: Use try-except\ntry:\n    first_item = my_list[0]\nexcept IndexError:\n    print('List is empty')\n\n# Method 3: Use len() to check\nif len(my_list) > 0:\n    first_item = my_list[0]\nelse:\n    print('List is empty')\n```\n\nWhich approach would work best for your specific use case?",
            ),
        ],
        metadata={"topic": "programming", "difficulty": "beginner"},
    )

    print("📝 Sample Conversation:")
    print("-" * 50)
    print(conversation.to_string())
    print()

    # Create evaluator with LLM-based metrics
    print("🤖 Initializing LLM-based metrics...")
    evaluator = Evaluator(metrics=[
        ConversationQualityMetric(threshold=0.7),
        ResponseHelpfulnessMetric(threshold=0.7),
        ResponseSafetyMetric(threshold=0.8),
    ])

    print("✅ Metrics initialized!")
    print()

    # Run evaluation
    print("🔍 Running LLM evaluation...")
    print("   This may take a few moments as we call the LLM...")
    print()

    try:
        report = evaluator.run(conversation)

        print("📊 Evaluation Results:")
        print("=" * 50)
        print(f"Overall Score: {report.overall_score:.2f}")
        print(f"Passed: {'✅ Yes' if report.passed else '❌ No'}")
        print()

        for result in report.results:
            print(f"📈 {result.metric_name.replace('_', ' ').title()}:")
            print(f"   Score: {result.score:.2f} {'✅' if result.passed else '❌'}")

            if result.error:
                print(f"   Error: {result.error}")

            if result.details:
                if "reasoning" in result.details:
                    print(f"   Reasoning: {result.details['reasoning']}")

                if "strengths" in result.details:
                    print(f"   Strengths: {', '.join(result.details['strengths'])}")

                if "weaknesses" in result.details:
                    print(
                        f"   Areas for improvement: {', '.join(result.details['weaknesses'])}"
                    )

                if (
                    "safety_concerns" in result.details
                    and result.details["safety_concerns"]
                ):
                    print(
                        f"   Safety concerns: {', '.join(result.details['safety_concerns'])}"
                    )
                elif "safety_concerns" in result.details:
                    print("   Safety concerns: None identified")

                if "risk_level" in result.details:
                    print(f"   Risk level: {result.details['risk_level']}")

            print()

        print("🎯 Summary:")
        passed_metrics = sum(1 for r in report.results if r.passed)
        total_metrics = len(report.results)
        print(f"   {passed_metrics}/{total_metrics} metrics passed")

    except Exception as e:
        print(f"❌ Error during evaluation: {e}")
        print("   Make sure your OPENAI_API_KEY is valid and you have API credits.")


if __name__ == "__main__":
    main()
