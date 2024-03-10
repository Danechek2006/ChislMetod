import math

def equation(x):
    return 4*x*(math.log(x)**2) - 4*math.sqrt(1+x) + 5

def combination_method(a, b, e):
    iterations = 0
    while True:
        iterations += 1
        fa = equation(a)
        fb = equation(b)
        c = (a * fb - b * fa) / (fb - fa)

        if equation(c) == 0.0 or (b - a) / 2 < e:
            break
        elif equation(c) * fa < 0:
            b = c
        else:
            a = c

    return c

accuracies = [10**-5, 10**-6, 10**-7, 10**-8, 10**-9, 10**-10]
a = 1.0
b = 2.0

for e in accuracies:
    root = combination_method(a, b, e)
    print(f"Точность: {e}, Корень уравнения: {root}")
