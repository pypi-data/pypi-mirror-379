"""Conversation coherence metric."""

from ...data.types import Conversation, EvaluationResult
from ..base import Metric


class ConversationCoherenceMetric(Metric):
    """Evaluates overall conversation coherence and flow."""

    def __init__(self, threshold: float = 0.6):
        """Initialize the conversation coherence metric."""
        super().__init__("conversation_coherence", threshold)

    def evaluate(self, conversation: Conversation) -> EvaluationResult:
        """Evaluate conversation coherence."""
        turns = conversation.turns

        if len(turns) < 2:
            return self._create_result(1.0, {"reason": "single_turn_conversation"})

        # Check for topic consistency across turns
        topic_consistency = self._calculate_topic_consistency(turns)

        # Check for proper conversation flow
        flow_score = self._calculate_flow_score(turns)

        # Combine scores
        coherence_score = (topic_consistency + flow_score) / 2

        details = {
            "topic_consistency": topic_consistency,
            "flow_score": flow_score,
            "total_turns": len(turns),
        }

        return self._create_result(coherence_score, details)

    def _calculate_topic_consistency(self, turns) -> float:
        """Calculate topic consistency across turns."""
        if len(turns) < 2:
            return 1.0

        # Simple word-based topic consistency
        all_words = []
        for turn in turns:
            all_words.extend(turn.content.lower().split())

        if not all_words:
            return 0.0

        # Count word frequency
        word_counts = {}
        for word in all_words:
            word_counts[word] = word_counts.get(word, 0) + 1

        # Calculate consistency based on word repetition
        total_words = len(all_words)
        unique_words = len(word_counts)

        if total_words == 0:
            return 0.0

        # Higher consistency when there's some word repetition
        consistency = min(1.0, unique_words / total_words)
        return 1.0 - consistency  # Invert so higher repetition = higher consistency

    def _calculate_flow_score(self, turns) -> float:
        """Calculate conversation flow score."""
        if len(turns) < 2:
            return 1.0

        flow_violations = 0
        total_transitions = len(turns) - 1

        for i in range(total_transitions):
            current_turn = turns[i]
            next_turn = turns[i + 1]

            # Check for abrupt topic changes (simple heuristic)
            current_words = set(current_turn.content.lower().split())
            next_words = set(next_turn.content.lower().split())

            if current_words and next_words:
                overlap = len(current_words.intersection(next_words))
                if overlap == 0 and len(current_words) > 3 and len(next_words) > 3:
                    flow_violations += 1

        return (
            1.0 - (flow_violations / total_transitions)
            if total_transitions > 0
            else 1.0
        )
