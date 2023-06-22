numberA = [1, 52, 36, 25, 8, -12]
numbers = sorted(numberA)
diff_a = 10**20

for i in range(len(numbers) - 1):
    if numbers[i + 1] - numbers[i] < diff_a:
        diff_a = numbers[i + 1] - numbers[i]

numberB = [3, -54, 232, 4, 76, 340]
numbers = sorted(numberB)
diff_b = 10**20

for i in range(len(numbers) - 1):
    if numbers[i + 1] - numbers[i] < diff_b:
        diff_b = numbers[i + 1] - numbers[i]

if diff_a > diff_b:
    print(f"The lowest different between two numbers is {diff_b}")
else:
    print(f"The lowest different between two numbers is {diff_a}")
