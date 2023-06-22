def convert_binary_to_decimal(user_input):
    return int(user_input, 2)


user_input = input("Enter a binary number: ")
if int(user_input[:1]) == 0:
    exit(
        "Note that your code must check and ensure that the input will not start with 0."
    )
decimal = convert_binary_to_decimal(user_input)

print(f"Decimal number: {decimal}")
