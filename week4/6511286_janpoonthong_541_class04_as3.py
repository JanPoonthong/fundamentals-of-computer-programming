count = 0
sum_of_even = 0
sum_of_odd = 0

while True:
    count += 1
    number = int(input(f"Number#{count}: "))

    if number == 0:
        break

    if number % 2 == 0:
        sum_of_even = sum_of_even + number
    else:
        sum_of_odd = sum_of_odd + number

print(f"The sum of all odd numbers is: {sum_of_odd}")
print(f"The sum of all even numbers is: {sum_of_even}")

if sum_of_odd > sum_of_even:
    print("The winner is the sum of all odd numbers")
elif sum_of_odd < sum_of_even:
    print("The winner is the sum of all even numbers")
else:
    print("No winner here. Try again")
