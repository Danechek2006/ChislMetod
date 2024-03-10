import math

def equation(x):
    return 4*x*(math.log(x)**2) - 4*math.sqrt(1+x) + 5

def bisection_method(a, b, e):
    if equation(a) * equation(b) >= 0:
        print("Нет корня в указанном интервале.")
        return None

    iterations = 0
    while (b - a) >= e:
        iterations += 1
        c = (a + b) / 2

        if equation(c) == 0.0:
            break
        elif equation(c) * equation(a) < 0:
            b = c
        else:
            a = c

    return c

accuracies = [10**-5, 10**-6, 10**-7, 10**-8, 10**-9, 10**-10]
a = 1.0
b = 2.0

for e in accuracies:
    root = bisection_method(a, b, e)
    print(f"Точность: {e}, Корень уравнения: {root}")
