list_1 = [3, 4]
list_2 = [3, 6, 7, 4]

if len(list_2) < len(list_1):
    for number in list_2:
        if number in list_1:
            print("Yes, list_2 is a subset of list_1")
            exit()
        else:
            print("No, list_2 is not a subset of list_1")
            exit()
elif len(list_1) < len(list_2):
    for number in list_1:
        if number in list_2:
            print("Yes, list_1 is a subset of list_2")
            exit()
        else:
            print("No, list_1 is not a subset of list_2")
            exit()
