def AlternateLetters(word1, word2):
    outword = ""
    if len(word1) < len(word2):
        for i in range(len(word1)):
            outword += word1[i] + word2[-(i + 1)] + "_"
    else:
        for i in range(len(word2)):
            outword += word1[i] + word2[-(i + 1)] + "_"
    return outword


word1 = input("Enter word#1: ")
word2 = input("Enter word#2: ")
print(f"The output is {AlternateLetters(word1, word2)}")
