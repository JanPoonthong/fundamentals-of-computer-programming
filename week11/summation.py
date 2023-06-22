def summationI(n):
    result = 1
    for each in range(1, n + 1):
        result *= each
    return result


def summationR(n):
    if n == 1:
        return 1
    else:
        return n + summationR(n + 1)


for i in range(31):
    print(f"{i}\t\t{summationI(i)}\t\t{summationR(i)}")
