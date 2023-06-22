def unHiddenMessage(inStr):
    word = ""
    for i in range(1, len(inStr)):
        if i * i >= len(inStr):
            break
        word += inStr[i * i]
    return word


print(unHiddenMessage("0H23E5678L012345P78901234!67890"))
print(unHiddenMessage("ahjwoeasdh'alksdoko"))
print(unHiddenMessage("0G2se4ws5t7rsa89_1234aaaai67890aswdht234567qxgkqa?9012"))
print(unHiddenMessage("0I23L5678O012345V78901234E"))
print(unHiddenMessage("0A23B5678A012345C21213213"))
