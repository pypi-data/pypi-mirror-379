"""
Main LabelingManager class for the Label Accelerator SDK.
"""
from typing import Dict, List, Optional, Union
import pandas as pd
from .core import Field, AdaptiveFormula
from .models import LabelingResult, PerformanceMetrics
from .license_validator import LicenseValidator

class LabelingManager:
    """
    Manages labeling functions (heuristics) and applies them to data
    to generate programmatic labels.
    """
    def __init__(self,
                 heuristics: List[Field],
                 positive_threshold: float = 0.7,
                 negative_threshold: float = 0.4,
                 tier: str = 'community',
                 license_key: Optional[str] = None):
        
        self.heuristics = heuristics
        self.positive_threshold = positive_threshold
        self.negative_threshold = negative_threshold
        self.tier = tier
        self.license_key = license_key
        self._setup_formula()

    def _setup_formula(self):
        """Initializes the core formula engine and validates the license."""
        
        # <-- MEJORA 1: Definir la identidad única de este SDK.
        sdk_identity = "DSF_Label"
        
        # <-- MEJORA 2: Pasar la identidad al validador.
        is_valid = LicenseValidator.validate_license(
            self.tier, 
            self.license_key, 
            sdk_identity
        )
        
        effective_tier = self.tier
        if not is_valid and self.tier != 'community':
            # <-- MEJORA 3: Mensaje de error más específico.
            print(f"Warning: Invalid or expired license for '{self.tier}' tier for {sdk_identity}. Falling back to community.")
            effective_tier = 'community'

        config = {h.name: h.to_dict() for h in self.heuristics}
        
        # Se inicializa la fórmula con el tier efectivo
        self.formula = AdaptiveFormula(config, effective_tier, self.license_key)
        
        # Se actualiza el tier del manager para consistencia
        self.tier = effective_tier

    def label(self, data: Dict[str, Any]) -> LabelingResult:
        """Applies heuristics to a single data point to generate a label."""
        score = self.formula.evaluate(data)

        if score >= self.positive_threshold:
            label = "POSITIVE"
            needs_review = False
        elif score < self.negative_threshold:
            label = "NEGATIVE"
            needs_review = False
        else:
            label = "ABSTAIN"
            needs_review = True

        return LabelingResult(label=label, score=score, needs_review=needs_review)

    def label_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Applies heuristics to a pandas DataFrame, adding 'label' and 'score' columns.
        (Professional / Enterprise feature)
        """
        if self.tier == 'community':
            raise PermissionError("DataFrame support requires a Professional or Enterprise license.")
        
        results = df.apply(lambda row: self.label(row.to_dict()), axis=1)
        df['label'] = [r.label for r in results]
        df['score'] = [r.score for r in results]
        df['needs_review'] = [r.needs_review for r in results]
        return df

    def get_metrics(self) -> Union[PerformanceMetrics, Dict]:
        """Gets performance and usage metrics for the labeling process."""
        metrics_dict = self.formula.get_metrics()
        if 'error' in metrics_dict:
            return metrics_dict
        return PerformanceMetrics(
            total_evaluations=metrics_dict.get('evaluations', 0),
            avg_score=metrics_dict.get('avg_score', 0),
            current_threshold=metrics_dict.get('current_confidence_level', 0.65),
            min_score=metrics_dict.get('min_score', 0),
            max_score=metrics_dict.get('max_score', 1),
            tier=metrics_dict.get('tier', 'community'),
            license_valid=metrics_dict.get('license_valid', False),
            adaptive_weights=metrics_dict.get('adaptive_weights', False),
            weight_changes=metrics_dict.get('weight_changes', {})
        )