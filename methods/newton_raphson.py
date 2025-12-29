# By Soltani Asma - Newton-Raphson Method
"""
Implementation of Newton-Raphson method for solving f(x) = 0.

This module provides a robust implementation of the Newton-Raphson iterative method
with comprehensive error handling and result tracking.
"""

import math
from typing import Callable, List, Tuple


class NewtonRaphsonResult:

    
    def __init__(self, root: float, iterations: int, errors: List[float],
                 converged: bool, message: str, sequence: List[float]):
        self.root = root
        self.iterations = iterations
        self.errors = errors
        self.converged = converged
        self.message = message
        self.sequence = sequence
    
    def __str__(self) -> str:
        return (f"Newton-Raphson Result:\n"
                f"  Root: {self.root:.10f}\n"
                f"  Iterations: {self.iterations}\n"
                f"  Final Error: {self.errors[-1] if self.errors else 0:.2e}\n"
                f"  Converged: {self.converged}\n"
                f"  Message: {self.message}")


def newton_raphson(f: Callable[[float], float],
                   df: Callable[[float], float],
                   x0: float,
                   epsilon: float = 1e-10,
                   max_iterations: int = 100,
                   tolerance_f: float = 1e-10) -> NewtonRaphsonResult:

    # Initialize variables
    xn = x0
    sequence = [x0]
    errors = []
    
    # Iteration loop
    for iteration in range(max_iterations):
        # Evaluate function and derivative at current point
        fx = f(xn)
        dfx = df(xn)
        
        # Check for zero derivative (method fails)
        if abs(dfx) < 1e-14:
            return NewtonRaphsonResult(
                root=xn,
                iterations=iteration,
                errors=errors,
                converged=False,
                message=f"Derivative too small at iteration {iteration}: df(x) = {dfx}",
                sequence=sequence
            )
        
        # Newton-Raphson iteration formula
        xn_plus_1 = xn - fx / dfx
        
        # Calculate error (distance between consecutive iterates)
        error = abs(xn_plus_1 - xn)
        errors.append(error)
        sequence.append(xn_plus_1)
        
        # Check convergence criteria
        # Criterion 1: |x_{n+1} - x_n| < epsilon
        # Criterion 2: |f(x_n)| < tolerance_f
        if error < epsilon and abs(fx) < tolerance_f:
            return NewtonRaphsonResult(
                root=xn_plus_1,
                iterations=iteration + 1,
                errors=errors,
                converged=True,
                message="Converged successfully",
                sequence=sequence
            )
        
        # Update for next iteration
        xn = xn_plus_1
    
    # Maximum iterations reached without convergence
    return NewtonRaphsonResult(
        root=xn,
        iterations=max_iterations,
        errors=errors,
        converged=False,
        message=f"Maximum iterations ({max_iterations}) reached without convergence",
        sequence=sequence
    )


if __name__ == "__main__":
    # Test example: Find √2
    f = lambda x: x**2 - 2
    df = lambda x: 2*x
    
    result = newton_raphson(f, df, x0=1.0, epsilon=1e-10)
    print(result)
    print(f"\n√2 ≈ {result.root:.10f}")
    print(f"Actual: {math.sqrt(2):.10f}")