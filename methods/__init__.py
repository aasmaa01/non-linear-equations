"""
Methods package for numerical equation solving.
Contains implementations of three iterative methods.
"""

from .newton_raphson import newton_raphson
from .dichotomy import dichotomy
from .successive_approximations import successive_approximations

__all__ = [
    'newton_raphson',
    'NewtonRaphsonResult',
    'dichotomy',
    'successive_approximations'
]