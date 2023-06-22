def easyencrypt(letter, shift, shift_direction):
    base = ord("a")

    lower_case = letter.lower()
    new_strs = [""]

    if shift_direction == "r":
        for character in lower_case:
            c = (ord(character) - base + shift) % 26
            new_strs.append(chr(c + base))
    elif shift_direction == "l":
        for character in lower_case:
            c = (ord(character) - base - shift) % 26
            new_strs.append(chr(c + base))
    return new_strs


def easydecrypt(en_strs, shift, shift_direction):
    base = ord("a")

    new_strs = [""]
    en_strs.pop(0)

    if shift_direction == "r":
        for character in en_strs:
            c = (ord(character) - base - shift) % 26
            new_strs.append(chr(c + base))
    elif shift_direction == "l":
        for character in en_strs:
            c = (ord(character) - base + shift) % 26
            new_strs.append(chr(c + base))

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
