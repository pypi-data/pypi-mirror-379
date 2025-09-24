"""LLM-based response helpfulness evaluation."""

import os

from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel

from ...data.types import Conversation, EvaluationResult
from ..base import Metric


class HelpfulnessEvaluation(BaseModel):
    """Structured output for helpfulness evaluation."""

    average_helpfulness: float = Field(
        description="Average helpfulness score across all responses (0-1)",
        ge=0.0,
        le=1.0,
    )
    individual_scores: list[float] = Field(
        description="Helpfulness score for each assistant response"
    )
    reasoning: str = Field(
        description="Brief explanation of the helpfulness assessment"
    )
    most_helpful_response: int = Field(
        description="Index of the most helpful response (0-based)"
    )
    least_helpful_response: int = Field(
        description="Index of the least helpful response (0-based)"
    )


class ResponseHelpfulnessMetric(Metric):
    """Evaluates response helpfulness using LLM-as-a-judge."""

    def __init__(
        self,
        name: str = "response_helpfulness",
        threshold: float = 0.7,
        model_name: str = "gpt-4o-mini",
        api_key: str | None = None,
    ):
        """Initialize the helpfulness metric.

        Args:
            name: Metric name
            threshold: Minimum score to pass (0.0 to 1.0)
            model_name: OpenAI model to use
            api_key: OpenAI API key (if None, uses OPENAI_API_KEY env var)
        """
        super().__init__(name, threshold)
        self.model_name = model_name
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")

        # Initialize agent lazily to avoid API key issues during import
        self.agent = None
        self._system_prompt = """You are an expert evaluator of AI assistant responses.
        Your task is to assess how helpful each assistant response is in the context of the conversation.

        Evaluate helpfulness based on:
        - Directly addressing the user's question or request
        - Providing useful, actionable information
        - Being specific and detailed when appropriate
        - Offering relevant examples or explanations
        - Following up appropriately on previous exchanges

        Provide scores from 0.0 (not helpful) to 1.0 (extremely helpful) for each response."""

    def _get_agent(self):
        """Get or create the LLM agent."""
        if self.agent is None:
            if not self.api_key:
                raise ValueError(
                    "OpenAI API key is required. Set OPENAI_API_KEY environment variable or pass api_key parameter."
                )

            # Create the LLM agent
            model = OpenAIChatModel(self.model_name)
            self.agent = Agent(model, output_type=HelpfulnessEvaluation)
            self.agent.system_prompt = self._system_prompt

        return self.agent

    def evaluate(self, conversation: Conversation) -> EvaluationResult:
        """Evaluate response helpfulness using LLM."""
        try:
            # Check if API key is available
            if not self.api_key:
                return self._create_result(
                    score=0.0,
                    error="OpenAI API key is required. Set OPENAI_API_KEY environment variable or pass api_key parameter.",
                )

            # Get only assistant responses for evaluation
            assistant_responses = conversation.assistant_turns
            if not assistant_responses:
                return self._create_result(
                    score=0.0, error="No assistant responses found in conversation"
                )

            # Format conversation for evaluation
            conversation_text = conversation.to_string()

            # Get LLM evaluation
            agent = self._get_agent()
            result = agent.run_sync(
                f"Please evaluate the helpfulness of each assistant response in this conversation:\n\n{conversation_text}"
            )

            if result.output is None:
                return self._create_result(
                    score=0.0, error="LLM evaluation failed - no response generated"
                )

            evaluation = result.output

            # Create detailed results
            details = {
                "average_helpfulness": evaluation.average_helpfulness,
                "individual_scores": evaluation.individual_scores,
                "reasoning": evaluation.reasoning,
                "most_helpful_response": evaluation.most_helpful_response,
                "least_helpful_response": evaluation.least_helpful_response,
                "model_used": self.model_name,
                "total_responses": len(assistant_responses),
            }

            return self._create_result(
                score=evaluation.average_helpfulness, details=details
            )

        except Exception as e:
            return self._create_result(
                score=0.0, error=f"LLM evaluation error: {str(e)}"
            )
