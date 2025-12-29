# Soltani Asma - main.py
"""
Projet d'Analyse Numérique - Résolution d'Équations Non Linéaires
Groupe: Soltani Asma, Triaki Hiba, Numidia

Programme principal avec menu interactif.
"""

import math
import os
from methods import newton_raphson, dichotomy, successive_approximations
from functions import get_test_function
from analysis import analyze_convergence, compare_methods, save_results
from plots import plot_convergence, plot_comparison


def print_separator():
    """Print a visual separator."""
    print("\n" + "="*70)


def print_header(method_name):
    """Print method header."""
    print_separator()
    print(f"  {method_name}")
    print_separator()


def run_newton():
    """Run Newton-Raphson method (Soltani Asma)."""
    print_header("MÉTHODE DE NEWTON-RAPHSON")

    test_func = get_test_function("sqrt2")
    x0 = 1.0
    epsilon = 1e-10

    print(f"Recherche de la racine de f(x) = {test_func.name}")
    print(f"Point initial x₀ = {x0}")
    print(f"Précision ε = {epsilon}")
    print("Formule : x_{n+1} = x_n - f(x_n)/f'(x_n)\n")

    result = newton_raphson(
        f=test_func.f,
        df=test_func.df,
        x0=x0,
        epsilon=epsilon
    )

    print(f"{'Résultats':-^70}")
    print(f"Solution approchée    : {result.root:.10f}")
    print(f"Valeur exacte (√2)    : {test_func.exact_root:.10f}")
    print(f"Erreur absolue        : {abs(result.root - test_func.exact_root):.2e}")
    print(f"Nombre d'itérations   : {result.iterations}")
    print("Convergence           : Quadratique (ordre 2)")
    print("Implémentée par       : Soltani Asma")

    analysis = analyze_convergence(result.sequence, test_func.exact_root)
    print(f"\nOrdre estimé          : {analysis['convergence_order']:.2f}")

    plot_convergence(result.errors, "Newton-Raphson")



def run_dichotomy():
    """Run Dichotomy method (Numidia)."""
    print_header("MÉTHODE DE DICHOTOMIE")

    test_func = get_test_function("sqrt2")
    a, b = test_func.interval
    epsilon = 1e-6

    print(f"Intervalle initial [{a}, {b}]")
    print(f"Précision ε = {epsilon}\n")

    root, iterations, history = dichotomy(
        f=test_func.f,
        a=a,
        b=b,
        epsilon=epsilon
    )

    print(f"{'Résultats':-^70}")
    print(f"Solution approchée    : {root:.10f}")
    print(f"Valeur exacte (√2)    : {test_func.exact_root:.10f}")
    print(f"Erreur absolue        : {abs(root - test_func.exact_root):.2e}")
    print(f"Nombre d'itérations   : {iterations}")
    print("Convergence           : Linéaire (ordre 1)")
    print("Implémentée par       : Numidia")


def run_successive_approximations():
    """Run Successive Approximations method (Triaki Hiba)."""
    print_header("MÉTHODE DES APPROXIMATIONS SUCCESSIVES")

    test_func = get_test_function("sqrt2")
    x0 = 1.0
    epsilon = 1e-6

    print("Méthode de Héron")
    print("φ(x) = 0.5 * (x + 2/x)")
    print(f"Point initial x₀ = {x0}")
    print(f"Précision ε = {epsilon}\n")

    root, iterations, sequence, errors = successive_approximations(
        phi=lambda x: 0.5 * (x + 2/x),
        x0=x0,
        epsilon=epsilon
    )

    print(f"{'Résultats':-^70}")
    print(f"Solution approchée    : {root:.10f}")
    print(f"Valeur exacte (√2)    : {test_func.exact_root:.10f}")
    print(f"Erreur absolue        : {abs(root - test_func.exact_root):.2e}")
    print(f"Nombre d'itérations   : {iterations}")
    print("Convergence           : Linéaire (ordre 1)")
    print("Implémentée par       : Triaki Hiba")





def main():
    while True:
        print_separator()
        print("RÉSOLUTION D'ÉQUATIONS NON LINÉAIRES")
        print("Choisissez une méthode :")
        print("  1 - Dichotomie")
        print("  2 - Approximations successives")
        print("  3 - Newton-Raphson")
        print("  0 - Quitter")
        print_separator()

        choice = input("Votre choix : ").strip()

        if choice == "1":
            run_dichotomy()
        elif choice == "2":
            run_successive_approximations()
        elif choice == "3":
            run_newton()
        elif choice == "0":
            print("\nFin du programme.")
            break
        else:
            print("\nChoix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()