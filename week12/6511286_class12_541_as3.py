def easyencrypt(letter, shift, shift_direction):
    base = ord("a")

    new_strs = [""]

    if shift_direction == "r":
        for character in letter:
            if character == " ":
                new_strs.append(character)
                continue
            if character.islower():
                c = (ord(character) - base + shift) % 26
                new_strs.append(chr(c + base))
            else:
                c = (ord(character) - ord("A") + shift) % 26
                new_strs.append(chr(c + ord("A")))
    elif shift_direction == "l":
        for character in letter:
            if character == " ":
                new_strs.append(character)
                continue
            if character.islower():
                c = (ord(character) - base - shift) % 26
                new_strs.append(chr(c + base))
            else:
                c = (ord(character) - ord("A") - shift) % 26
                new_strs.append(chr(c + ord("A")))
    return new_strs


def easydecrypt(en_strs, shift, shift_direction):
    base = ord("a")

    new_strs = [""]
    en_strs.pop(0)

    if shift_direction == "r":
        for character in en_strs:
            if character == " ":
                new_strs.append(character)
                continue
            if character.islower():
                c = (ord(character) - base - shift) % 26
                new_strs.append(chr(c + base))
            else:
                c = (ord(character) - ord("A") - shift) % 26
                new_strs.append(chr(c + ord("A")))
    elif shift_direction == "l":
        for character in en_strs:
            if character == " ":
                new_strs.append(character)
                continue
            if character.islower():
                c = (ord(character) - base + shift) % 26
                new_strs.append(chr(c + base))
            else:
                c = (ord(character) - ord("A") + shift) % 26
                new_strs.append(chr(c + ord("A")))

    return new_strs


letter = input(
    "Enter the message you want to encrypt (only alphabet and no space): "
)
shift = int(input("The number you want to shift by: "))
shift_direction = input("Enter a shift direction: ")

en_strs = easyencrypt(letter, shift, shift_direction)
print(en_strs)
de_str = easydecrypt(en_strs, shift, shift_direction)
print(de_str)
