def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


print(combination(7, 3))
