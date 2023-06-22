user_number = int(input("Input number: "))
revs = 0

while user_number > 0:
    remainder = user_number % 10
    revs = (revs * 10) + remainder
    user_number //= 10
print(revs)
