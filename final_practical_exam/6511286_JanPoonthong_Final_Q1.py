def SublistSearch(mat, key):
    search, loopcount = linearSearch(key, mat)
    return search, loopcount


def linearSearch(key, ls):
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            for l in range(len(ls) - 1, -1, -1):
                for k in range(len(ls[i]) - 1, -1, -1):
                    if ls[i][j] == key:
                        return [i + 1, j + 1]
                    elif ls[l][k] == key:
                        return [l + 1, k + 1]
    return [-1, -1]


mat = [[1, 2, 3, 4, 5, 6], [9, 10, 11, 12, 13, 14], [21, 22, 23, 24, 25, 26]]
key = int(input("Enter a number you want to search: "))
row, column = SublistSearch(mat, key)
print("For matrix")
for m in mat:
    print(m)
print("========================")
if row != -1:
    print(f"The key, {key}, found at row#{row} and column#{column}.")
else:
    print(f"Sorry {key} could not be found.")
