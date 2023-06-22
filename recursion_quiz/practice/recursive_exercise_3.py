def sumdigits(n):
    if len(str(n)) == 1:
        return int(str(n)[:1])
    else:
        return int(str(n)[:1]) + sumdigits(int(str(n)[1:]))


print(sumdigits(345))
