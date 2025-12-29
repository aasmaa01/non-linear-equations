# By Triaki hiba 242431461313 - Successive Approximations

import math

def phi(x):
    return 0.5 * (x + 2/x)

x0 = 1.0
eps = 1e-6
n = 0

while True:
    x1 = phi(x0)
    n += 1
    if abs(x1 - x0) < eps:
        break
    x0 = x1

print("Solution approx =", round(x1, 6))
print("Nombre d'iterations =", n)
print("Convergence : lineaire (ordre 1)")
