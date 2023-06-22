numX = int(input("Enter first num: "))
numY = int(input("Enter second num: "))
numZ = int(input("Enter second num: "))

if numX <= numY <= numZ or numZ <= numY <= numX:
    print(numY)
elif numY <= numX <= numZ or numZ <= numX <= numY:
    print(numX)
else:
    print(numZ)
