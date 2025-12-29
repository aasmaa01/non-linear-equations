"""
Iteration tracking and comparison utilities.
"""

from typing import List, Dict, Any
import json
import os


def track_iterations(method_name: str, sequence: List[float], 
                    errors: List[float], converged: bool) -> Dict[str, Any]:

    return {
        'method': method_name,
        'iterations': len(sequence) - 1,
        'converged': converged,
        'final_value': sequence[-1],
        'sequence': sequence,
        'errors': errors
    }


def compare_methods(results: Dict[str, Any]) -> str:
 
    report = "\n" + "="*70 + "\n"
    report += "  COMPARISON OF METHODS\n"
    report += "="*70 + "\n\n"
    
    report += f"{'Method':<30} {'Iterations':>12} {'Converged':>12} {'Final Value':>15}\n"
    report += "-"*70 + "\n"
    
    for method_name, result in results.items():
        converged_str = "Yes" if result.get('converged', True) else "No"
        iterations = result.get('iterations', 0)
        final_val = result.get('root', result.get('final_value', 0))
        
        report += f"{method_name:<30} {iterations:>12} {converged_str:>12} {final_val:>15.10f}\n"
    
    return report


def save_results(results: Dict[str, Any], filename: str = "results/comparison.json"):

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Convert to serializable format
    serializable = {}
    for method, result in results.items():
        serializable[method] = {
            'iterations': result.get('iterations', 0),
            'converged': result.get('converged', True),
            'final_value': result.get('root', result.get('final_value', 0))
        }
    
    with open(filename, 'w') as f:
        json.dump(serializable, f, indent=2)


if __name__ == "__main__":
    # Test
    results = {
        'Newton': {'iterations': 4, 'converged': True, 'root': 1.414213562},
        'Dichotomy': {'iterations': 20, 'converged': True, 'root': 1.414214},
    }
    print(compare_methods(results))