user_input = input("Enter a distance (in km or mi): ")


def DistanceConversion(input):
    global result, length
    count = 0
    number = ""
    for integer in user_input:
        if integer in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            number += integer
            count += 1

    length = user_input[count:]

    if length == "km":
        result = int(number) // 1.609
    elif length == "mi":
        result = int(number) * 1.609


print(DistanceConversion(user_input))
if length == "km":
    print(f"{user_input} is equal to {round(result)}mi")
else:
    print(f"{user_input} is equal to {round(result)}km")
