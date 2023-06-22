import math

basketball_volume = 455.9
number = float(input("Enter a number: "))
volume = 4 / 3 * math.pi * math.pow(number, 3)

if volume > basketball_volume:
    print("The  entered  radius  is  too  big")
else:
    print("The entered  radius  is  OK")
