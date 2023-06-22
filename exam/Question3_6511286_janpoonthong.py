user = input("Enter a sentence: ")
vowel = ""
space = ""
left_over = ""

for i in user:
    if i == " ":
        space += i
    elif i in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        vowel += i
    else:
        left_over += i

print(f"({space}){left_over}({vowel})")
