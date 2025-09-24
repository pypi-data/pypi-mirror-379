"""Batch evaluation example for Turnwise."""

import json

from turnwise import (
    ConversationCoherenceMetric,
    ConversationDataset,
    ConversationLengthMetric,
    Evaluator,
    ResponseRelevanceMetric,
    create_summary_report,
)


def main():
    """Demonstrate batch evaluation with Turnwise."""

    # Sample conversation data (could be loaded from JSON file)
    conversation_data = [
        {
            "turns": [
                {"role": "user", "content": "Hello, how are you?"},
                {
                    "role": "assistant",
                    "content": "I'm doing well, thank you! How can I help you today?",
                },
                {"role": "user", "content": "I need help with Python programming"},
                {
                    "role": "assistant",
                    "content": "I'd be happy to help with Python! What specific aspect would you like to work on?",
                },
            ],
            "metadata": {"session_id": "001", "topic": "programming"},
        },
        {
            "turns": [
                {"role": "user", "content": "What's the weather like?"},
                {
                    "role": "assistant",
                    "content": "I don't have access to real-time weather data, but I can help you find weather information online.",
                },
                {"role": "user", "content": "That's okay, thanks anyway"},
                {
                    "role": "assistant",
                    "content": "You're welcome! Feel free to ask if you need help with anything else.",
                },
            ],
            "metadata": {"session_id": "002", "topic": "weather"},
        },
        {
            "turns": [
                {"role": "user", "content": "Tell me a joke"},
                {
                    "role": "assistant",
                    "content": "Why don't scientists trust atoms? Because they make up everything!",
                },
                {"role": "user", "content": "Haha, that's funny!"},
                {
                    "role": "assistant",
                    "content": "I'm glad you enjoyed it! Would you like to hear another one?",
                },
            ],
            "metadata": {"session_id": "003", "topic": "entertainment"},
        },
    ]

    # Create dataset directly from data
    dataset = ConversationDataset(conversation_data)
    print(f"Created dataset with {len(dataset)} conversations")

    # Create evaluator with metrics
    evaluator = Evaluator(metrics=[
        ConversationLengthMetric(min_turns=2, max_turns=10),
        ResponseRelevanceMetric(threshold=0.6),
        ConversationCoherenceMetric(threshold=0.7),
    ])

    # Evaluate all conversations
    print("\nEvaluating conversations...")
    reports = evaluator.batch(dataset)

    # Display individual results
    print("\n=== Individual Results ===")
    for i, report in enumerate(reports):
        print(
            f"\nConversation {i + 1} ({report.conversation.metadata.get('topic', 'unknown')}):"
        )
        print(f"  Overall Score: {report.overall_score:.3f}")
        print(f"  Status: {'PASSED' if report.passed else 'FAILED'}")

        for result in report.results:
            status = "✓" if result.passed else "✗"
            print(f"    {status} {result.metric_name}: {result.score:.3f}")

    # Create and display summary report
    print("\n=== Summary Report ===")
    summary = create_summary_report(reports)

    print(f"Total Conversations: {summary['total_conversations']}")
    print(f"Passed Conversations: {summary['passed_conversations']}")
    print(f"Overall Pass Rate: {summary['overall_pass_rate']:.1%}")
    print(f"Average Overall Score: {summary['average_overall_score']:.3f}")

    print("\nMetric Statistics:")
    for metric_name, stats in summary["metric_statistics"].items():
        print(f"  {metric_name}:")
        print(f"    Pass Rate: {stats['pass_rate']:.1%}")
        print(f"    Average Score: {stats['average_score']:.3f}")
        print(f"    Score Range: {stats['min_score']:.3f} - {stats['max_score']:.3f}")
        if stats["error_count"] > 0:
            print(f"    Errors: {stats['error_count']}")

    # Save results to JSON file
    output_data = []
    for i, report in enumerate(reports):
        output_data.append(
            {
                "conversation_index": i,
                "overall_score": report.overall_score,
                "passed": report.passed,
                "results": [
                    {
                        "metric_name": r.metric_name,
                        "score": r.score,
                        "passed": r.passed,
                        "details": r.details,
                        "error": r.error,
                    }
                    for r in report.results
                ],
                "metadata": report.metadata,
            }
        )

    with open("evaluation_results.json", "w") as f:
        json.dump(output_data, f, indent=2)

    print("\nResults saved to evaluation_results.json")


if __name__ == "__main__":
    main()
