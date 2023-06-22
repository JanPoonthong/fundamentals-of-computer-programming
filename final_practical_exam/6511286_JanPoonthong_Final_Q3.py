def keepCenter2or3(list):
    if len(list) > 2 and len(list) % 2 != 0:
        return [
            list[((len(list) - 1) // 2) - 1],
            list[(len(list) - 1) // 2],
            list[((len(list) - 1) // 2) + 1],
        ]
    elif len(list) > 2 and len(list) % 2 == 0:
        return [list[(len(list) - 1) // 2], list[((len(list) - 1) // 2) + 1]]
    elif len(list) < 3:
        return list


print(keepCenter2or3([1, 2, 3, 4, 5, 6, 7, 8]))
print(keepCenter2or3([12, 3, 5, 78, 9]))
print(keepCenter2or3([1, 3]))
print(keepCenter2or3([1, 2, 3, 4, 5, 6, 7]))
print(keepCenter2or3([12, 3, 5, 78]))
print(keepCenter2or3([1, 2, 3]))
