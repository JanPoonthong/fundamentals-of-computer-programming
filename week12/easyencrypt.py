def easyencrypt(letter, shift):
    base = ord("a")

    lower_case = letter.lower()
    new_strs = [""]

    for character in lower_case:
        c = (ord(character) - base + shift) % 26
        new_strs.append(chr(c + base))

    return new_strs


letter = input(
    "Enter the message you want to encrypt (only alphabet and no space): "
)
shift = int(input("The number you want to shift by: "))
encrypted_text = easyencrypt(letter, shift)

print(encrypted_text)
