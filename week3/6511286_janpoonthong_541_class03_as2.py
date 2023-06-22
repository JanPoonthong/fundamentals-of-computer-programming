x1 = int(input("Enter the first number: "))
x2 = int(input("Enter the second number: "))
x3 = int(input("Enter the third number: "))
x4 = int(input("Enter the fourth number: "))

sum_num = x1 + x2 + x3 + x4

print(f"The sum is: {sum_num}")

if sum_num % 2 == 0 and sum_num > 0:
    print(f"{sum_num} is Positive Even")
elif sum_num == 0:
    print("0 is Zero")
else:
    print("Negative Odd")
