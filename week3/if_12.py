number = int(input("Enter a number: "))

if number < 2:
    print("The person is baby")
elif 2 <= number <= 4:
    print("The person is toddler")
elif 4 <= number <= 13:
    print("The person is a kid")
elif 13 <= number <= 20:
    print("The person is a teenager")
elif 20 <= number <= 64:
    print("The person is an adult")
elif number >= 65:
    print("The person is an elder")
