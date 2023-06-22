def foursliceSearch(key, numlist):
    sliceIndex = int(len(numlist) / 4)
    count = 0
    while len(numlist) >= 1:
        for x in range(sliceIndex):
            if key == numlist[x]:
                return count + 1
        count += 1
        numlist = numlist[sliceIndex:]
    return count


def bidirectionSearch(key, numlist):
    numlist.sort()
    size = len(numlist)
    leftMost = 0
    rightMost = size - 1
    count = 1
    while True:
        middle = round((leftMost + rightMost) / 2)
        if key == numlist[middle]:
            return f"It takes {count} loops to find {key}."
        elif key < numlist[middle]:
            rightMost = middle - 1
            count += 1
        else:
            leftMost = middle + 1
            count += 1
        if leftMost > rightMost:
            return "Not Found"


key = 9
numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print(foursliceSearch(key, numlist))
print(bidirectionSearch(key, numlist))
