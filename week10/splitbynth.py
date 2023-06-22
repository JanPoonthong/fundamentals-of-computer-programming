def splitByNth(inStr, n):
    a = []
    for i in range(0, len(inStr), n):
        a.append(inStr[i : i + n])
    return a


print(splitByNth("hello there this is an example", 3))
