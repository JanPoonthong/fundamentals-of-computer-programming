myList = [1, 2, 3, 4, 6, 7, 8]
sortedList = sorted(myList)
count = 1
longest = 1
for i in range(len(sortedList) - 1):
    if sortedList[i + 1] == sortedList[i] + 1:
        count += 1
    else:
        count = 1
    if count > longest:
        longest = count
print(longest)
