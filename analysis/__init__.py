"""
Analysis package for convergence studies.
"""

from .convergence import analyze_convergence, convergence_order
from .iterations import track_iterations, compare_methods

__all__ = [
    'analyze_convergence',
    'convergence_order',
    'track_iterations',
    'compare_methods'
]