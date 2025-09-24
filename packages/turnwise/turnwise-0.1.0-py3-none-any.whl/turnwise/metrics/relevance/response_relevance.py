"""Response relevance metric."""

from ...data.types import Conversation, EvaluationResult, Role
from ..base import Metric


class ResponseRelevanceMetric(Metric):
    """Evaluates if assistant responses are relevant to user inputs."""

    def __init__(self, threshold: float = 0.7):
        """Initialize the response relevance metric."""
        super().__init__("response_relevance", threshold)

    def evaluate(self, conversation: Conversation) -> EvaluationResult:
        """Evaluate response relevance using simple keyword matching."""
        user_turns = conversation.user_turns
        assistant_turns = conversation.assistant_turns

        if not user_turns or not assistant_turns:
            return self._create_result(0.0, {"reason": "insufficient_turns"})

        relevance_scores = []

        # Match each assistant response to the most recent user input
        for i, assistant_turn in enumerate(assistant_turns):
            # Find the most recent user turn before this assistant turn
            user_input = ""
            for j in range(len(conversation.turns)):
                if conversation.turns[j] == assistant_turn:
                    # Look backwards for the most recent user turn
                    for k in range(j - 1, -1, -1):
                        if conversation.turns[k].role == Role.USER:
                            user_input = conversation.turns[k].content
                            break
                    break

            if not user_input:
                relevance_scores.append(0.0)
                continue

            # Simple keyword-based relevance scoring
            user_words = set(user_input.lower().split())
            response_words = set(assistant_turn.content.lower().split())

            if not user_words:
                relevance_scores.append(0.0)
                continue

            # Calculate word overlap
            overlap = len(user_words.intersection(response_words))
            relevance = overlap / len(user_words)
            relevance_scores.append(relevance)

        avg_relevance = (
            sum(relevance_scores) / len(relevance_scores) if relevance_scores else 0.0
        )

        details = {
            "individual_scores": relevance_scores,
            "average_relevance": avg_relevance,
            "total_responses": len(assistant_turns),
        }

        return self._create_result(avg_relevance, details)
