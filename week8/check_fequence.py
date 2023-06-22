def check(list):
    res = None
    max = 0
    for i in list:
        freq = list.count(i)
        if freq > max:
            max = freq
            res = i
    return res


print(check([1, 2, 3, 1, 4, 4, 4, 4, 4, 4, 4, 3]))
