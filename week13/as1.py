def fourslicebidirectionalSearch(ls, key):
  count = 0
  for x in range(len(ls)):
    count += 1
    for y in range(len(ls[x])):
      if ls[x][y] == key or ls[x][-y-1] == 1:
        return count
  return 'Key not found'

ls = [13,43,2,4,45,7,4,5,6,4,5,3,3,4,4,3,3,43,3,1,4]
newLs = []
i = 4
for x in range(len(ls) // 4 + 1):
  newLs.append(ls[i-4:i])
  i += 4

key = 3
print('Key found in sublist No. -> ', end="")
print(fourslicebidirectionalSearch(newLs, key))