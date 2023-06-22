for i in range(1, 10):
    for j in range(1, 10):
        number = i * j
        if number % 2 == 1:
            print("--", end=" ")
        else:
            print("%2d" % (number), end=" ")
    print("")


print("")

for i in range(1, 10):
    for j in range(1, 10):
        number = i * j
        first_number = number // 10
        second_number = number % 10
        if first_number % 2 == 1 or second_number % 2 == 1:
            print("--", end=" ")
        else:
            print("%2d" % (number), end=" ")
    print("")
