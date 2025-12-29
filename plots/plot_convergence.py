"""
Convergence plotting utilities.
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import List, Dict, Any
import os


def plot_convergence(sequence: List[float], errors: List[float], 
                     method_name: str, exact_root: float = None,
                     save_path: str = None):
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot 1: Sequence convergence
    iterations = range(len(sequence))
    ax1.plot(iterations, sequence, 'bo-', label='Approximations')
    
    if exact_root is not None:
        ax1.axhline(y=exact_root, color='r', linestyle='--', label='Exact root')
    
    ax1.set_xlabel('Iteration')
    ax1.set_ylabel('Value')
    ax1.set_title(f'{method_name}: Sequence Convergence')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Error decay
    iterations_error = range(1, len(errors) + 1)
    ax2.semilogy(iterations_error, errors, 'ro-', label='Error')
    ax2.set_xlabel('Iteration')
    ax2.set_ylabel('Error (log scale)')
    ax2.set_title(f'{method_name}: Error Decay')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {save_path}")
    else:
        plt.show()


def plot_comparison(results: Dict[str, Any], exact_root: float = None,
                   save_path: str = None):
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    for method_name, result in results.items():
        errors = result.get('errors', [])
        if errors:
            iterations = range(1, len(errors) + 1)
            ax.semilogy(iterations, errors, 'o-', label=method_name, linewidth=2)
    
    ax.set_xlabel('Iteration', fontsize=12)
    ax.set_ylabel('Error (log scale)', fontsize=12)
    ax.set_title('Convergence Comparison of Different Methods', fontsize=14, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Comparison plot saved to {save_path}")
    else:
        plt.show()


if __name__ == "__main__":
    # Test
    import math
    sequence = [1.0, 1.5, 1.416666667, 1.414215686, 1.414213562]
    errors = [0.5, 0.0833, 0.00694, 0.0000212, 1.97e-10]
    
    plot_convergence(sequence, errors, "Newton-Raphson", 
                    exact_root=math.sqrt(2))