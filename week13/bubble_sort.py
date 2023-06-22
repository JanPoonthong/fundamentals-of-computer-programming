def bubbleSort(ls):
    n = len(ls)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]


import random

randomlist = []
for i in range(0, 10000):
    n = random.randint(1, 1000000000)
    randomlist.append(n)
print(randomlist)

bubbleSort(randomlist)

print(randomlist)
