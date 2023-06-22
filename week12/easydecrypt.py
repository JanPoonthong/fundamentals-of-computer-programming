import easyencrypt


def easydecrypt(en_strs, shift):
    base = ord("a")

    new_strs = [""]
    en_strs.pop(0)

    for character in en_strs:
        c = (ord(character) - base - shift) % 26
        new_strs.append(chr(c + base))

    return new_strs


en_strs = easyencrypt.easyencrypt(easyencrypt.letter, easyencrypt.shift)
print("Encrypted text is: ", "".join(en_strs))

de_strs = easydecrypt(en_strs, easyencrypt.shift)
print("Decrypted text is: ", "".join(de_strs))
