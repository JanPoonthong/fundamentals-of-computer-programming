data = [10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25]
for i in range(31):
    if i % 3 == 0 and not i in data:
        print(i, end=" ")
    elif i in data:
        print("_", end=" ")
    else:
        print("*", end=" ")
