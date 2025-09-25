"""
Defines heuristic presets for common weak supervision tasks.
"""
from typing import List
from .core import Field

class HeuristicPresets:
    """Provides ready-to-use heuristic configurations."""

    @staticmethod
    def spam_detection_heuristics() -> List[Field]:
        """Heuristics for identifying SPAM text."""
        return [
            Field(name='contains_link', reference=True, importance=3.0, sensitivity=2.0),
            Field(name='contains_spam_keywords', reference=True, importance=5.0, sensitivity=5.0),
            Field(name='text_length', reference=50, importance=2.0, sensitivity=1.5),
            Field(name='is_all_caps', reference=True, importance=4.0, sensitivity=4.0),
            Field(name='digit_ratio', reference=0.1, importance=3.0, sensitivity=3.0),
        ]

    @staticmethod
    def sentiment_analysis_heuristics() -> List[Field]:
        """Heuristics for basic sentiment analysis."""
        return [
            Field(name='positive_word_count', reference=5, importance=4.0, sensitivity=2.0),
            Field(name='negative_word_count', reference=0, importance=4.0, sensitivity=3.0),
            Field(name='has_negation', reference=False, importance=3.0, sensitivity=5.0),
            Field(name='has_intensifier', reference=True, importance=2.0, sensitivity=1.5),
        ]