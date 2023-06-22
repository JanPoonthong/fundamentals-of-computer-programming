name = input("Enter a word: ")

name = name.upper()
a = f"**={name}=**"
length = len(a)

for i in range(length):
    print("*", end="")

print()

for i in range(len(name)):
    print(a)

for i in range(length):
    print("*", end="")
