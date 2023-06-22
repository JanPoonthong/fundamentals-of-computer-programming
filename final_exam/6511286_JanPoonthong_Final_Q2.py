zeroCount = 0
total = 0
oddList = []
evenList = []
while True:
    try:
        myNum = int(input("Enter an integer: "))
    except ValueError:
        print("=============================")
        print("Not an integer! Try again.")
        print("=============================")
        continue
    else:
        if myNum == 0:
            zeroCount += 1

        if zeroCount >= 3:
            break
        if myNum % 2 == 0:
            if myNum == 0:
                continue
            evenList.append(myNum)
        elif myNum % 2 == 1:
            oddList.append(myNum)
        
        total += myNum

        oddList.sort()
        evenList.sort()

print(f"Total is {total}.")
print(f"Oddlist is {oddList}")
print(f"Evenlist {evenList}")