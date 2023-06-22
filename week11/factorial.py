def factorialI(n):
    result = 1
    for each in range(1, n + 1):
        result *= each
    return result


print(factorialI(4))


def factorialR(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorialR(n - 1)


print("n\tf(n) by Iterative\tf(n) by Recursive")
for i in range(31):
    print(f"{i}\t\t{factorialI(i)}\t\t{factorialR(i)}")
