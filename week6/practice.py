str1 = "This is test"
str2 = "test"

if str2 in str1:
    print("Yes, some str2 is in str1")
else:
    print("Oh no")


name = "Trudy"

if name not in "Alice,Bob":
    print("Access denied")
else:
    print("Access granted")


x = "Hello World"
print(x[0:5])
print(x[6:11])

print("Alice".find("ice"))
print("Alice".replace("ice", "ex"))
print("3".isalpha())
print("Alice,Bob".split(","))
print(",".join(["Alice", "Bob"]))

sentence = input("Write a sentence: ").upper()
print(sentence)
