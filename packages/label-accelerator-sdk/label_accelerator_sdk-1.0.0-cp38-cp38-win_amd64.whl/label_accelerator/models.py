"""
Data models for the Label Accelerator SDK.
"""

from dataclasses import dataclass
from typing import Dict, Optional, Any

# POSITIVE, NEGATIVE, o ABSTAIN (necesita revisión humana)
Label = str

@dataclass
class LabelingResult:
    """Represents the result of a programmatic labeling function."""
    label: Label
    score: float
    needs_review: bool

@dataclass
class PerformanceMetrics:
    """Represents performance and usage metrics for the SDK."""
    total_evaluations: int
    avg_score: float
    current_threshold: float
    min_score: float
    max_score: float
    tier: str = 'community'
    license_valid: bool = False
    adaptive_weights: bool = False
    weight_changes: Optional[Dict[str, float]] = None