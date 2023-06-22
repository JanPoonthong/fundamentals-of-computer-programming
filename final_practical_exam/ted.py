def SublistSearch(mat, key):
    last_search_index = len(mat[0]) - 1
    mid_point_length = round(len(mat[0]) / 2)
    for i in range(len(mat)):
        for j in range(mid_point_length):
            if mat[i][j] == key:
                return i + 1, j + 1
            if mat[i][last_search_index - j] == key:
                return i + 1, last_search_index - j + 1
    return -1, -1


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
