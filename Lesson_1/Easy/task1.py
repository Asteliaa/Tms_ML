import math

def solve_quadratic(a, b, c):
    D = b**2 - 4*a*c
    if D < 0:
        return 'Нет действительных корней'
    elif D == 0:
        return [-b / (2*a)]
    else:
        return [(-b + math.sqrt(D)) / (2*a), (-b - math.sqrt(D)) / (2*a)]

quadratic_equations = [
    (1, -12, 20),
    (1, 17, 72),
    (1, -7, -44),
    (1, 9, 8),
    (1, -2, -63)
]

solutions = [solve_quadratic(a, b, c) for (a, b, c) in quadratic_equations]
print(solutions)
