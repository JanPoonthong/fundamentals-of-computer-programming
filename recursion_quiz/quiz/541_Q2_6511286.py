def SumSkip37(numList):
    if len(numList) == 0:
        return 0
    elif numList[0] % 3 == 0 or numList[0] % 7 == 0:
        return SumSkip37(numList[1:])
    else:
        return numList[0] + SumSkip37(numList[1:])


numList = [1, 3, 5, 7, 9]
print(f"The result is {SumSkip37(numList)}.")
