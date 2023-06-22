def bunnyEars(n):
    if n == 0:
        return 0
    else:
        return 2 + bunnyEars(n - 1)


for i in range(21):
    print(bunnyEars(i))
