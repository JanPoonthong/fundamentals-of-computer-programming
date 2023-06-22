def bidirectionSearch(key, ls):
    ls.sort()
    size = len(ls)
    leftMost = 0
    rightMost = size - 1
    loopcount = 0

    while True:
        loopcount += 1
        middle = round((leftMost + rightMost) / 2)
        if key == ls[middle]:
            print(f"{loopcount} loops to find {key}")
            return True
        elif key < ls[middle]:
            rightMost = middle - 1
        else:
            leftMost = middle + 1
        if leftMost > rightMost:
            print("Sorry a number is not found")
            return False


bidirectionSearch(
    2, [1, 3, 4, 653, 324, 234, 23, 43423, 2, 1312, 31, 23, 12, 3123, 123, 12]
)


def linearSearch(key, ls):
    last_search_index = len(ls) - 1
    mid_point_length = round(len(ls) / 2)
    loopcount = 0
    for j in range(mid_point_length):
        loopcount += 1
        if ls[j] == key:
            return j + 1, loopcount
        if ls[last_search_index - j] == key:
            return last_search_index - j + 1, loopcount
    return -1, -1


column, loopcount = linearSearch(69, [1, 2, 3, 4, 5, 69, 1, 23, 123, 123])
print(column, loopcount)
