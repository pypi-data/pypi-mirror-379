"""LLM-based conversation quality evaluation."""

import os

from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel

from ...data.types import Conversation, EvaluationResult
from ..base import Metric


class QualityEvaluation(BaseModel):
    """Structured output for quality evaluation."""

    overall_score: float = Field(
        description="Overall conversation quality score (0-1)", ge=0.0, le=1.0
    )
    reasoning: str = Field(description="Brief explanation of the quality assessment")
    strengths: list[str] = Field(description="List of conversation strengths")
    weaknesses: list[str] = Field(description="List of areas for improvement")


class ConversationQualityMetric(Metric):
    """Evaluates overall conversation quality using LLM-as-a-judge."""

    def __init__(
        self,
        name: str = "conversation_quality",
        threshold: float = 0.7,
        model_name: str = "gpt-4o-mini",
        api_key: str | None = None,
    ):
        """Initialize the quality metric.

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
        self._system_prompt = """You are an expert evaluator of AI conversations.
        Your task is to assess the overall quality of a multi-turn conversation between a user and an AI assistant.

        Evaluate based on:
        - Clarity and coherence of responses
        - Helpfulness and relevance to user needs
        - Natural conversation flow
        - Appropriate tone and style
        - Problem-solving effectiveness

        Provide a score from 0.0 (poor) to 1.0 (excellent) and explain your reasoning."""

    def _get_agent(self):
        """Get or create the LLM agent."""
        if self.agent is None:
            if not self.api_key:
                raise ValueError(
                    "OpenAI API key is required. Set OPENAI_API_KEY environment variable or pass api_key parameter."
                )

            # Create the LLM agent
            model = OpenAIChatModel(self.model_name)
            self.agent = Agent(model, output_type=QualityEvaluation)
            self.agent.system_prompt = self._system_prompt

        return self.agent

    def evaluate(self, conversation: Conversation) -> EvaluationResult:
        """Evaluate conversation quality using LLM."""
        try:
            # Check if API key is available
            if not self.api_key:
                return self._create_result(
                    score=0.0,
                    error="OpenAI API key is required. Set OPENAI_API_KEY environment variable or pass api_key parameter.",
                )

            # Format conversation for evaluation
            conversation_text = conversation.to_string()

            # Get LLM evaluation
            agent = self._get_agent()
            result = agent.run_sync(
                f"Please evaluate this conversation:\n\n{conversation_text}"
            )

            if result.output is None:
                return self._create_result(
                    score=0.0, error="LLM evaluation failed - no response generated"
                )

            evaluation = result.output

            # Create detailed results
            details = {
                "overall_score": evaluation.overall_score,
                "reasoning": evaluation.reasoning,
                "strengths": evaluation.strengths,
                "weaknesses": evaluation.weaknesses,
                "model_used": self.model_name,
                "conversation_length": len(conversation.turns),
            }

            return self._create_result(score=evaluation.overall_score, details=details)

        except Exception as e:
            return self._create_result(
                score=0.0, error=f"LLM evaluation error: {str(e)}"
            )
