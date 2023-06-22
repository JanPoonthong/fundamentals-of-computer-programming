x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))
x3 = int(input("Enter x3: "))

if x1 % x3 == 0 and x2 % x3 == 0:
    print("x3 is a factor of both x1 and x2")
elif x1 % x3 == 0:
    print("x3 is a factor of x1")
elif x2 % x3 == 0:
    print("x3 is a factor of x2")
else:
    print("x3 is neither a factor of x1 nor x2")
