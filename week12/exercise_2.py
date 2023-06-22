def mid(x, y, z):
    list = [x, y, z]
    list.sort()
    return list[1]


user_input = input(
    "Enter a 3 number with comma separating the number, for example:1,2,3: "
).split(",")

print(mid(user_input[0], user_input[1], user_input[2]))
