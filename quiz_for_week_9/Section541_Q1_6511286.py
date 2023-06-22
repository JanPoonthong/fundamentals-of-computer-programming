strList = input("Enter words: ").split(" ")

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

newList = []

for word in strList:
    newList.append(" ")
    for character in word:
        if character in vowels:
            continue
        else:
            newList.append(character)

count = 0
output_one = ""
for char in newList:
    if count == 0:
        count += 1
    else:
        output_one += char

print(f"Output 1 = {output_one}")

output_two = ""
for char in output_one.split(" "):
    if len(char) < 3:
        output_two += "*" * len(char) + " "
    elif len(char) >= 3:
        output_two += char + " "

print(f"Output 2 = {output_two}")
# Do your best for this quiz. OK?!!!
# Anakin does not believe in JEDI FORCE.
