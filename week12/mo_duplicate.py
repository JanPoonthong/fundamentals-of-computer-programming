def MoDuplicate(int_list):
    newli = []
    # sort automatic
    seen = set()
    for item in li:
        if item not in seen:
            seen.add(item)
            newli.append(item)
        elif item in seen and item % 2 != 0:
            item = item * 10
            seen.add(item)
            newli.append(item)
        else:
            item = item * 20
            seen.add(item)
            newli.append(item)

    return newli


li = [1, 1, 3, 5, 4, 5, 4, 9, 4, 8, 6]
print(li)
li = MoDuplicate(li)
print(li)
