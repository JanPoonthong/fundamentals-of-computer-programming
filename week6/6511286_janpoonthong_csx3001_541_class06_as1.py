user_input = input("Enter string: ")

upper = 0
lower = 0
space = 0
a = ""
for i in user_input:
    if i.isupper():
        upper += 1
        a += i.lower()
    elif i.islower():
        lower += 1
        a += i.upper()
    elif i == " ":
        space += 1
        a += " "

print()

print(f"{upper} Uppercase")
print(f"{lower} Lowercase")
print(f"{space} Spaces")
print(a, end="")
