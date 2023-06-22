def isOdd(number):
    if number % 2 == 1:
        return True
    return False


user_input = int(input("Enter a number: "))
print(isOdd(user_input))
