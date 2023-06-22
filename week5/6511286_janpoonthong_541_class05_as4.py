numbers = [100, 10, 200, 25, 7, 20]

numbers = sorted(numbers)
diff = 10**20

for i in range(len(numbers) - 1):
    if numbers[i + 1] - numbers[i] < diff:
        diff = numbers[i + 1] - numbers[i]

print(f"The lowest different between two numbers is {diff}")
