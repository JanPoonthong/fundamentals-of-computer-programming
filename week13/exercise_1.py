def summation(n):
    if len(n) == 0:
        return 0
    elif n[0] % 3 == 0 and n[0] % 7 == 0:
        return summation(n[1:])
    else:
        return n[0] + summation(n[1:])


print(summation([1, 3]))
