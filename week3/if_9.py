number = input("Enter a number: ")

x = 0
for i in number:
    x = x + int(i)

if x % 2 == 0:
    print("Sum  of  all  digits  is  an  even number")
else:
    print("Sum of all digits is not an even number")
