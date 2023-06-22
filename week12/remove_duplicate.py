def removeDuplicate(li):
    newli = []
    # sort automatic
    seen = set()
    for item in li:
        if item not in seen:
            seen.add(item)
            newli.append(item)
    print(li)
    return newli


li = [1, 1, 3, 5, 4, 5, 5, 9, 4, 8, 6]
print(li)
li = removeDuplicate(li)
print(li)
