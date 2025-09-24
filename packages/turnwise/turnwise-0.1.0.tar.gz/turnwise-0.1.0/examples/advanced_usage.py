"""Advanced usage example showing the new Turnwise structure."""

from turnwise import (
    Conversation,
    ConversationCoherenceMetric,
    ConversationLengthMetric,
    Evaluator,
    ResponseRelevanceMetric,
    Role,
    Turn,
    config,
)


def main():
    """Demonstrate advanced Turnwise usage with the new structure."""

    # Create a conversation
    conversation = Conversation(
        turns=[
            Turn(role=Role.USER, content="What is machine learning?"),
            Turn(
                role=Role.ASSISTANT,
                content="Machine learning is a subset of artificial intelligence that enables computers to learn and improve from experience without being explicitly programmed.",
            ),
            Turn(role=Role.USER, content="Can you give me an example?"),
            Turn(
                role=Role.ASSISTANT,
                content="Sure! Image recognition is a common example. When you upload a photo to social media and it automatically tags your friends, that's machine learning at work.",
            ),
            Turn(role=Role.USER, content="That's interesting! How does it work?"),
            Turn(
                role=Role.ASSISTANT,
                content="The system is trained on thousands of labeled photos. It learns patterns like facial features, and then can identify similar patterns in new, unlabeled photos.",
            ),
        ],
        metadata={"session_id": "demo_001", "topic": "machine_learning"},
    )

    # Create evaluator with metrics and custom configuration
    evaluator = Evaluator(
        metrics=[
            ConversationLengthMetric(min_turns=2, max_turns=20, threshold=0.8),
            ResponseRelevanceMetric(threshold=0.7),
            ConversationCoherenceMetric(threshold=0.6),
        ],
        max_workers=2
    )

    print("=== Advanced Turnwise Evaluation ===")
    print(f"Configuration: {config.to_dict()}")
    print()

    # Evaluate with custom metadata
    metadata = {
        "evaluation_id": "demo_001",
        "model_version": "1.0.0",
        "timestamp": "2024-01-01T00:00:00Z",
    }

    print("Evaluating conversation...")
    report = evaluator.run(conversation, metadata, parallel=True)

    # Display results
    print("\n=== Evaluation Results ===")
    print(f"Overall Score: {report.overall_score:.3f}")
    print(f"Status: {'PASSED' if report.passed else 'FAILED'}")
    print(f"Total Turns: {len(conversation.turns)}")
    print(f"Metadata: {report.metadata}")
    print()

    print("Metric Results:")
    for result in report.results:
        status = "✓" if result.passed else "✗"
        print(
            f"  {status} {result.metric_name}: {result.score:.3f} (threshold: {result.passed})"
        )
        if result.details:
            print(f"    Details: {result.details}")
        if result.error:
            print(f"    Error: {result.error}")

    print("\nConversation:")
    print(conversation.to_string())

    # Show available metrics
    print("\n=== Available Metrics ===")
    print("Built-in metrics:")
    print("  • ConversationLengthMetric - Evaluates conversation length")
    print("  • ResponseRelevanceMetric - Checks response relevance")
    print("  • ConversationCoherenceMetric - Evaluates conversation flow")
    print("\nYou can also create custom metrics by extending the Metric base class!")


if __name__ == "__main__":
    main()
