"""Tests for core types."""

import pytest

from turnwise import Conversation, EvaluationReport, EvaluationResult, Role, Turn


class TestTurn:
    """Test Turn class."""

    def test_turn_creation(self):
        """Test creating a turn."""
        turn = Turn(role=Role.USER, content="Hello")
        assert turn.role == Role.USER
        assert turn.content == "Hello"
        assert turn.metadata is None

    def test_turn_with_metadata(self):
        """Test creating a turn with metadata."""
        metadata = {"timestamp": "2024-01-01"}
        turn = Turn(role=Role.ASSISTANT, content="Hi there", metadata=metadata)
        assert turn.metadata == metadata

    def test_empty_content_raises_error(self):
        """Test that empty content raises ValueError."""
        with pytest.raises(ValueError, match="Turn content cannot be empty"):
            Turn(role=Role.USER, content="")

        with pytest.raises(ValueError, match="Turn content cannot be empty"):
            Turn(role=Role.USER, content="   ")


class TestConversation:
    """Test Conversation class."""

    def test_conversation_creation(self):
        """Test creating a conversation."""
        turns = [
            Turn(role=Role.USER, content="Hello"),
            Turn(role=Role.ASSISTANT, content="Hi there!"),
        ]
        conv = Conversation(turns=turns)
        assert len(conv.turns) == 2
        assert conv.metadata is None

    def test_conversation_with_metadata(self):
        """Test creating a conversation with metadata."""
        turns = [Turn(role=Role.USER, content="Hello")]
        metadata = {"session_id": "123"}
        conv = Conversation(turns=turns, metadata=metadata)
        assert conv.metadata == metadata

    def test_empty_conversation_raises_error(self):
        """Test that empty conversation raises ValueError."""
        with pytest.raises(
            ValueError, match="Conversation must have at least one turn"
        ):
            Conversation(turns=[])

    def test_conversation_must_start_with_user_or_system(self):
        """Test that conversation must start with user or system turn."""
        turns = [Turn(role=Role.ASSISTANT, content="Hello")]
        with pytest.raises(
            ValueError, match="Conversation must start with user or system turn"
        ):
            Conversation(turns=turns)

    def test_user_turns_property(self):
        """Test user_turns property."""
        turns = [
            Turn(role=Role.USER, content="Hello"),
            Turn(role=Role.ASSISTANT, content="Hi"),
            Turn(role=Role.USER, content="How are you?"),
        ]
        conv = Conversation(turns=turns)
        user_turns = conv.user_turns
        assert len(user_turns) == 2
        assert user_turns[0].content == "Hello"
        assert user_turns[1].content == "How are you?"

    def test_assistant_turns_property(self):
        """Test assistant_turns property."""
        turns = [
            Turn(role=Role.USER, content="Hello"),
            Turn(role=Role.ASSISTANT, content="Hi"),
            Turn(role=Role.USER, content="How are you?"),
            Turn(role=Role.ASSISTANT, content="I'm good!"),
        ]
        conv = Conversation(turns=turns)
        assistant_turns = conv.assistant_turns
        assert len(assistant_turns) == 2
        assert assistant_turns[0].content == "Hi"
        assert assistant_turns[1].content == "I'm good!"

    def test_last_assistant_turn_property(self):
        """Test last_assistant_turn property."""
        turns = [
            Turn(role=Role.USER, content="Hello"),
            Turn(role=Role.ASSISTANT, content="Hi"),
            Turn(role=Role.USER, content="How are you?"),
            Turn(role=Role.ASSISTANT, content="I'm good!"),
        ]
        conv = Conversation(turns=turns)
        last_turn = conv.last_assistant_turn
        assert last_turn is not None
        assert last_turn.content == "I'm good!"

    def test_last_assistant_turn_none(self):
        """Test last_assistant_turn when no assistant turns exist."""
        turns = [Turn(role=Role.USER, content="Hello")]
        conv = Conversation(turns=turns)
        assert conv.last_assistant_turn is None

    def test_to_string(self):
        """Test to_string method."""
        turns = [
            Turn(role=Role.USER, content="Hello"),
            Turn(role=Role.ASSISTANT, content="Hi there!"),
        ]
        conv = Conversation(turns=turns)
        expected = "user: Hello\nassistant: Hi there!"
        assert conv.to_string() == expected


class TestEvaluationResult:
    """Test EvaluationResult class."""

    def test_evaluation_result_creation(self):
        """Test creating an evaluation result."""
        result = EvaluationResult(
            metric_name="test_metric", score=0.8, passed=True, details={"key": "value"}
        )
        assert result.metric_name == "test_metric"
        assert result.score == 0.8
        assert result.passed is True
        assert result.details == {"key": "value"}
        assert result.error is None


class TestEvaluationReport:
    """Test EvaluationReport class."""

    def test_evaluation_report_creation(self):
        """Test creating an evaluation report."""
        turns = [Turn(role=Role.USER, content="Hello")]
        conv = Conversation(turns=turns)

        results = [
            EvaluationResult(metric_name="metric1", score=0.8, passed=True),
            EvaluationResult(metric_name="metric2", score=0.6, passed=False),
        ]

        report = EvaluationReport(
            conversation=conv, results=results, overall_score=0.7, passed=False
        )

        assert report.conversation == conv
        assert len(report.results) == 2
        assert report.overall_score == 0.7
        assert report.passed is False

    def test_failed_metrics_property(self):
        """Test failed_metrics property."""
        results = [
            EvaluationResult(metric_name="metric1", score=0.8, passed=True),
            EvaluationResult(metric_name="metric2", score=0.6, passed=False),
        ]

        turns = [Turn(role=Role.USER, content="Hello")]
        conv = Conversation(turns=turns)
        report = EvaluationReport(
            conversation=conv, results=results, overall_score=0.7, passed=False
        )

        failed = report.failed_metrics
        assert len(failed) == 1
        assert failed[0].metric_name == "metric2"

    def test_passed_metrics_property(self):
        """Test passed_metrics property."""
        results = [
            EvaluationResult(metric_name="metric1", score=0.8, passed=True),
            EvaluationResult(metric_name="metric2", score=0.6, passed=False),
        ]

        turns = [Turn(role=Role.USER, content="Hello")]
        conv = Conversation(turns=turns)
        report = EvaluationReport(
            conversation=conv, results=results, overall_score=0.7, passed=False
        )

        passed = report.passed_metrics
        assert len(passed) == 1
        assert passed[0].metric_name == "metric1"
