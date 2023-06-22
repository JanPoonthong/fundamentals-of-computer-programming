def sum_integer(n):
    if len(n) == 1:
        return n[0]
    else:
        return n[0] + sum_integer(n[1:])


sum_integer([1, 2, 3])
