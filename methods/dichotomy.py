def f(x):
    return x*2 - 2

def dichotomy(f, a, b, epsilon):
    history = []
    iterations = 0
    while b - a > epsilon:
        m = (a + b) / 2
        if f(m) * f(a) < 0:
            b = m
        else:
            a = m
        history.append((a, b, m))
        iterations += 1
    root = (a + b) / 2
    return root, iterations, history
