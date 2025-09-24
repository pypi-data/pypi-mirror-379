"""Tests for metrics."""

from turnwise import (
    Conversation,
    ConversationCoherenceMetric,
    ConversationLengthMetric,
    ResponseRelevanceMetric,
    Role,
    Turn,
)


class TestConversationLengthMetric:
    """Test ConversationLengthMetric."""

    def test_appropriate_length_passes(self):
        """Test that appropriate length conversations pass."""
        turns = [
            Turn(role=Role.USER, content="Hello"),
            Turn(role=Role.ASSISTANT, content="Hi there!"),
        ]
        conv = Conversation(turns=turns)
        metric = ConversationLengthMetric(min_turns=1, max_turns=10)
        result = metric.evaluate(conv)

        assert result.passed is True
        assert result.score == 1.0
        assert result.metric_name == "conversation_length"

    def test_too_short_fails(self):
        """Test that too short conversations fail."""
        turns = [Turn(role=Role.USER, content="Hello")]
        conv = Conversation(turns=turns)
        metric = ConversationLengthMetric(min_turns=2, max_turns=10)
        result = metric.evaluate(conv)

        assert result.passed is False
        assert result.score == 0.0
        assert result.details["reason"] == "too_short"

    def test_too_long_fails(self):
        """Test that too long conversations fail."""
        turns = [Turn(role=Role.USER, content=f"Message {i}") for i in range(15)]
        conv = Conversation(turns=turns)
        metric = ConversationLengthMetric(min_turns=1, max_turns=10)
        result = metric.evaluate(conv)

        assert result.passed is False
        assert result.score == 0.0
        assert result.details["reason"] == "too_long"

    def test_custom_threshold(self):
        """Test custom threshold."""
        turns = [Turn(role=Role.USER, content="Hello")]
        conv = Conversation(turns=turns)
        metric = ConversationLengthMetric(min_turns=2, max_turns=10, threshold=0.0)
        result = metric.evaluate(conv)

        assert result.passed is True  # Should pass with threshold 0.0
        assert result.score == 0.0


class TestResponseRelevanceMetric:
    """Test ResponseRelevanceMetric."""

    def test_relevant_responses_pass(self):
        """Test that relevant responses pass."""
        turns = [
            Turn(role=Role.USER, content="What is the weather like?"),
            Turn(role=Role.ASSISTANT, content="The weather is sunny and warm today."),
        ]
        conv = Conversation(turns=turns)
        metric = ResponseRelevanceMetric(threshold=0.5)
        result = metric.evaluate(conv)

        assert result.passed is True
        assert result.score > 0.5

    def test_irrelevant_responses_fail(self):
        """Test that irrelevant responses fail."""
        turns = [
            Turn(role=Role.USER, content="What is the weather like?"),
            Turn(role=Role.ASSISTANT, content="I like pizza and ice cream."),
        ]
        conv = Conversation(turns=turns)
        metric = ResponseRelevanceMetric(threshold=0.5)
        result = metric.evaluate(conv)

        assert result.passed is False
        assert result.score < 0.5

    def test_insufficient_turns_handling(self):
        """Test handling of insufficient turns."""
        turns = [Turn(role=Role.USER, content="Hello")]
        conv = Conversation(turns=turns)
        metric = ResponseRelevanceMetric()
        result = metric.evaluate(conv)

        assert result.passed is False
        assert result.score == 0.0
        assert result.details["reason"] == "insufficient_turns"

    def test_empty_user_input_handling(self):
        """Test handling of minimal user input."""
        turns = [
            Turn(role=Role.USER, content="Hello"),
            Turn(role=Role.ASSISTANT, content="Hi there!"),
            Turn(role=Role.USER, content="a"),  # Minimal user input
            Turn(role=Role.ASSISTANT, content="How can I help?"),
        ]
        conv = Conversation(turns=turns)
        metric = ResponseRelevanceMetric()
        result = metric.evaluate(conv)

        # Should handle gracefully
        assert result.score >= 0.0


class TestConversationCoherenceMetric:
    """Test ConversationCoherenceMetric."""

    def test_coherent_conversation_passes(self):
        """Test that coherent conversations pass."""
        turns = [
            Turn(role=Role.USER, content="What is machine learning?"),
            Turn(role=Role.ASSISTANT, content="Machine learning is a subset of AI."),
            Turn(role=Role.USER, content="Can you give me an example?"),
            Turn(
                role=Role.ASSISTANT,
                content="Sure! Image recognition is a common example.",
            ),
        ]
        conv = Conversation(turns=turns)
        metric = ConversationCoherenceMetric(threshold=0.2)  # Lower threshold for test
        result = metric.evaluate(conv)

        assert result.passed is True
        assert result.score > 0.2

    def test_incoherent_conversation_fails(self):
        """Test that incoherent conversations fail."""
        turns = [
            Turn(role=Role.USER, content="What is machine learning?"),
            Turn(role=Role.ASSISTANT, content="I like pizza and ice cream."),
            Turn(role=Role.USER, content="Tell me about quantum physics."),
            Turn(role=Role.ASSISTANT, content="The weather is nice today."),
        ]
        conv = Conversation(turns=turns)
        metric = ConversationCoherenceMetric(threshold=0.5)
        result = metric.evaluate(conv)

        assert result.passed is False
        assert result.score < 0.5

    def test_single_turn_conversation_passes(self):
        """Test that single turn conversations pass."""
        turns = [Turn(role=Role.USER, content="Hello")]
        conv = Conversation(turns=turns)
        metric = ConversationCoherenceMetric()
        result = metric.evaluate(conv)

        assert result.passed is True
        assert result.score == 1.0
        assert result.details["reason"] == "single_turn_conversation"
