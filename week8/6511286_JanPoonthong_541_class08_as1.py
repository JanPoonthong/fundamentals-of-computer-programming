# 1) Write a Python program to sum all the items in a list

user_input = input("Enter a word: ").split(" ")
count = 0

for i in user_input:
    if i[0] == i[-1] and i[1] == i[-2]:
        count += 1
print(count)
