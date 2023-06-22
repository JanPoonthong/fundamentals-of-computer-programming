def even_number(n):
    if len(n) == 0:
        return 0
    elif n[0] % 2 == 1:
        return even_number(n[1:])
    else:
        return n[0] + even_number(n[1:])


print(even_number([2, 1, 4]))
