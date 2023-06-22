count_one = 1
number = 1

while count_one <= 12:
    print(f"\tx*{count_one}", end="")
    count_one += 1

print("")

while number <= 12:
    print(f"x = {number}", end="")
    m = 1
    while m <= 12:
        print(f"\t{number * m}", end="")
        m += 1
    print()
    number += 1
