"""Tests for LLM-based metrics."""

from unittest.mock import MagicMock, patch

from turnwise import (
    Conversation,
    ConversationQualityMetric,
    ResponseHelpfulnessMetric,
    ResponseSafetyMetric,
    Role,
    Turn,
)


class TestConversationQualityMetric:
    """Test ConversationQualityMetric."""

    def test_metric_initialization(self):
        """Test metric initialization."""
        metric = ConversationQualityMetric()
        assert metric.name == "conversation_quality"
        assert metric.threshold == 0.7
        assert metric.model_name == "gpt-4o-mini"

    def test_metric_with_custom_params(self):
        """Test metric with custom parameters."""
        metric = ConversationQualityMetric(
            name="custom_quality", threshold=0.8, model_name="gpt-4", api_key="test-key"
        )
        assert metric.name == "custom_quality"
        assert metric.threshold == 0.8
        assert metric.model_name == "gpt-4"
        assert metric.api_key == "test-key"

    @patch("turnwise.metrics.llm.quality.OpenAIChatModel")
    def test_evaluate_success(self, mock_model_class):
        """Test successful evaluation."""
        # Mock the LLM response
        mock_result = MagicMock()
        mock_result.output = MagicMock()
        mock_result.output.overall_score = 0.85
        mock_result.output.reasoning = "Good conversation flow"
        mock_result.output.strengths = ["Clear responses", "Helpful"]
        mock_result.output.weaknesses = ["Could be more detailed"]

        mock_agent = MagicMock()
        mock_agent.run_sync.return_value = mock_result

        metric = ConversationQualityMetric(api_key="test-key")
        metric.agent = mock_agent

        # Create test conversation
        conv = Conversation(
            turns=[
                Turn(role=Role.USER, content="Hello"),
                Turn(role=Role.ASSISTANT, content="Hi there!"),
            ]
        )

        result = metric.evaluate(conv)

        assert result.passed is True
        assert result.score == 0.85
        assert result.metric_name == "conversation_quality"
        assert "reasoning" in result.details
        assert "strengths" in result.details
        assert "weaknesses" in result.details

    def test_evaluate_no_llm_response(self):
        """Test evaluation when LLM returns no response."""
        metric = ConversationQualityMetric(api_key="test-key")
        metric.agent = MagicMock()
        metric.agent.run_sync.return_value = MagicMock(output=None)

        conv = Conversation(
            turns=[
                Turn(role=Role.USER, content="Hello"),
                Turn(role=Role.ASSISTANT, content="Hi there!"),
            ]
        )

        result = metric.evaluate(conv)

        assert result.passed is False
        assert result.score == 0.0
        assert "LLM evaluation failed" in result.error


class TestResponseHelpfulnessMetric:
    """Test ResponseHelpfulnessMetric."""

    def test_metric_initialization(self):
        """Test metric initialization."""
        metric = ResponseHelpfulnessMetric()
        assert metric.name == "response_helpfulness"
        assert metric.threshold == 0.7
        assert metric.model_name == "gpt-4o-mini"

    def test_evaluate_no_assistant_responses(self):
        """Test evaluation with no assistant responses."""
        metric = ResponseHelpfulnessMetric(api_key="test-key")

        conv = Conversation(
            turns=[
                Turn(role=Role.USER, content="Hello"),
                Turn(role=Role.USER, content="How are you?"),
            ]
        )

        result = metric.evaluate(conv)

        assert result.passed is False
        assert result.score == 0.0
        assert "No assistant responses found" in result.error


class TestResponseSafetyMetric:
    """Test ResponseSafetyMetric."""

    def test_metric_initialization(self):
        """Test metric initialization."""
        metric = ResponseSafetyMetric()
        assert metric.name == "response_safety"
        assert metric.threshold == 0.8
        assert metric.model_name == "gpt-4o-mini"

    @patch("turnwise.metrics.llm.safety.OpenAIChatModel")
    def test_evaluate_success(self, mock_model_class):
        """Test successful safety evaluation."""
        # Mock the LLM response
        mock_result = MagicMock()
        mock_result.output = MagicMock()
        mock_result.output.overall_safety_score = 0.95
        mock_result.output.is_safe = True
        mock_result.output.safety_concerns = []
        mock_result.output.risk_level = "low"
        mock_result.output.reasoning = "No safety concerns identified"

        mock_agent = MagicMock()
        mock_agent.run_sync.return_value = mock_result

        metric = ResponseSafetyMetric(api_key="test-key")
        metric.agent = mock_agent

        # Create test conversation
        conv = Conversation(
            turns=[
                Turn(role=Role.USER, content="Hello"),
                Turn(role=Role.ASSISTANT, content="Hi there!"),
            ]
        )

        result = metric.evaluate(conv)

        assert result.passed is True
        assert result.score == 0.95
        assert result.metric_name == "response_safety"
        assert result.details["is_safe"] is True
        assert result.details["risk_level"] == "low"
        assert result.details["safety_concerns"] == []
