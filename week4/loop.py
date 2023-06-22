count = 0
sum_number = 0

while 1 > 0:
    number = int(
        input(
            "Enter a positive integer (to terminate enter a negative number): "
        )
    )

    if number < 0:  # check if number is negative
        break

    # counting positive number
    count += 1
    # summing the number
    sum_number = sum_number + number

print(f"The total number of positive integers entered is {count}")
print(f"The sum of all positive integer(s) is {sum_number}")
