"""
Test functions for numerical methods.
"""

import math
from typing import Callable, Tuple


class TestFunction:
    """Container for a test function with its derivative."""
    
    def __init__(self, f: Callable, df: Callable, name: str, 
                 interval: Tuple[float, float], exact_root: float = None):
        self.f = f
        self.df = df
        self.name = name
        self.interval = interval
        self.exact_root = exact_root
    
    def __str__(self):
        return f"TestFunction: {self.name}"


def get_test_function(name: str = "sqrt2") -> TestFunction:
    """
    Get a predefined test function.
    
    Parameters:
    -----------
    name : str
        Name of test function: 'sqrt2', 'cubic', 'transcendental'
    
    Returns:
    --------
    TestFunction
        Function object with f, df, and metadata
    """
    
    if name == "sqrt2":
        # f(x) = x² - 2 = 0, root = √2
        return TestFunction(
            f=lambda x: x**2 - 2,
            df=lambda x: 2*x,
            name="x² - 2",
            interval=(0.0, 2.0),
            exact_root=math.sqrt(2)
        )
    
    elif name == "cubic":
        # f(x) = x³ - x - 2 = 0
        return TestFunction(
            f=lambda x: x**3 - x - 2,
            df=lambda x: 3*x**2 - 1,
            name="x³ - x - 2",
            interval=(1.0, 2.0),
            exact_root=1.5213797068045676  # Approximate
        )
    
    elif name == "transcendental":
        # f(x) = x - cos(x) = 0
        return TestFunction(
            f=lambda x: x - math.cos(x),
            df=lambda x: 1 + math.sin(x),
            name="x - cos(x)",
            interval=(0.0, 1.0),
            exact_root=0.7390851332151607  # Approximate
        )
    
    else:
        raise ValueError(f"Unknown test function: {name}")


if __name__ == "__main__":
    # Test
    tf = get_test_function("sqrt2")
    print(tf)
    print(f"f(√2) = {tf.f(tf.exact_root)}")