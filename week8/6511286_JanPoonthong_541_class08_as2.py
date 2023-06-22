# 2. Write a Python code to print unique stringsfrom the entered stringinputs.
user_input = input("Input: ").split(" ")

duplicates = []

for i in user_input:
    if i not in duplicates:
        duplicates.append(i)

print(duplicates)
