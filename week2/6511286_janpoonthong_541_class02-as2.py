number = int(input("Enter 3-digit number: "))
revs_number = 0

while number > 0:
    remainder = number % 10
    revs_number = (revs_number * 10) + remainder
    number = number // 10

print(revs_number)
