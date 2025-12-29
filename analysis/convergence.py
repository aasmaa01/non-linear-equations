"""
Convergence analysis utilities.
"""

import math
from typing import List, Tuple
import numpy as np


def convergence_order(errors: List[float]) -> float:
 
    if len(errors) < 3:
        return 1.0
    
    # Use last few errors for stability
    n = min(5, len(errors) - 1)
    errors = errors[-n-1:]
    
    # Filter out very small errors
    errors = [max(e, 1e-15) for e in errors]
    
    # Linear regression on log-log plot
    log_errors = [math.log(e) for e in errors]
    
    orders = []
    for i in range(len(log_errors) - 1):
        if log_errors[i] != 0:
            order = log_errors[i+1] / log_errors[i]
            orders.append(order)
    
    return np.mean(orders) if orders else 1.0


def analyze_convergence(sequence: List[float], exact_root: float = None) -> dict:
    """
    Analyze convergence properties of a sequence.
    
    Parameters:
    -----------
    sequence : List[float]
        Sequence of approximations
    exact_root : float, optional
        Exact root if known
    
    Returns:
    --------
    dict
        Analysis results including order, errors, etc.
    """
    n = len(sequence)
    
    # Calculate successive errors
    successive_errors = [abs(sequence[i+1] - sequence[i]) for i in range(n-1)]
    
    result = {
        'iterations': n - 1,
        'successive_errors': successive_errors,
        'final_value': sequence[-1],
        'convergence_rate': successive_errors[-1] / successive_errors[-2] if len(successive_errors) > 1 else None
    }
    
    if exact_root is not None:
        absolute_errors = [abs(x - exact_root) for x in sequence]
        result['absolute_errors'] = absolute_errors
        result['final_error'] = absolute_errors[-1]
        result['convergence_order'] = convergence_order(absolute_errors[1:])
    
    return result


if __name__ == "__main__":
    # Test with Newton sequence for √2
    import math
    sequence = [1.0, 1.5, 1.416666667, 1.414215686, 1.414213562]
    result = analyze_convergence(sequence, math.sqrt(2))
    print(f"Convergence order: {result['convergence_order']:.2f}")