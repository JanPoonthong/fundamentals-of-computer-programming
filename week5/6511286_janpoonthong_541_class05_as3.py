a = int(input("Enter a: "))
b = int(input("Enter b: "))

sum_number = 0
for i in range(a, b + 1):
    first_number = i // 10
    second_number = i % 10
    if i % 10 == 3 or i % 10 == 7:
        print("*", end=" ")
    elif first_number + second_number > 7:
        print("%", end=" ")
    else:
        print(i, end=" ")
