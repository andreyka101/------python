def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x * 2, y)
print(f(1, 12) * f(12, 25) * f(25, 40))