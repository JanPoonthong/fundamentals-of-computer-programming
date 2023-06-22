nList = [[2, 5, 99, 99], [-3, 8, 1, 2, 10], [1, 7, 100, 10]]


output = [[], [], []]
count = 0
for i in range(len(nList)):
    for j in range(len(nList[i])):
        if nList[i][j] % 2 == 0:
            output[count].append(nList[i][j])
    count += 1

print(f"Output: oddList = {output}")


output = [[], [], []]
count = 0
for i in range(len(nList)):
    for j in range(len(nList[i])):
        if nList[i][j] % 2 == 1:
            output[count].append(nList[i][j])
    count += 1

print(f"Output: oddList = {output}")
