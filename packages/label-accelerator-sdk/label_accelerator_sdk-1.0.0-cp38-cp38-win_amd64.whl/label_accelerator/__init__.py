"""
Label Accelerator SDK - Programmatic Labeling & Weak Supervision
"""

# Reusable fallback logic
try:
    from .core import Field, AdaptiveFormula
    _BACKEND = "Cython (Optimized)"
except ImportError:
    from .core_py import Field, AdaptiveFormula
    _BACKEND = "Pure Python"

# Alias 'Field' to 'Heuristic' for domain clarity
Heuristic = Field

# Public API for this specific SDK
from .labeler import LabelingManager
from .heuristics import HeuristicPresets
from .models import LabelingResult, PerformanceMetrics

__version__ = "1.0.0"

__all__ = [
    'LabelingManager',
    'Heuristic',
    'LabelingResult',
    'PerformanceMetrics',
    'HeuristicPresets',
    'get_backend'
]

def get_backend():
    """Returns which backend is being used ('Cython' or 'Pure Python')."""
    return _BACKEND