import math

def equation(x):
    return 4*x*(math.log(x)**2) - 4*math.sqrt(1+x) + 5

def chord_method(e):
    a = 1.0
    b = 2.0
    max_iterations = 1000
    iterations = 0

    while abs(b - a) > e and iterations < max_iterations:
        c = (a * equation(b) - b * equation(a)) / (equation(b) - equation(a))
        if equation(c) == 0:
            break
        elif equation(a) * equation(c) < 0:
            b = c
        else:
            a = c
        iterations += 1

    return c

accuracies = [10**-5, 10**-6, 10**-7, 10**-8, 10**-9, 10**-10]

for e in accuracies:
    root = chord_method(e)
    print(f"Точность: {e}, Корень уравнения: {root}")
