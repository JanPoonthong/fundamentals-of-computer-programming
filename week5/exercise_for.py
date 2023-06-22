for i in range(1, 13):
    print(f"\tx*{i}", end="")

print("")
for i in range(1, 13):
    print(f"x = {i}", end="")
    for m in range(1, 13):
        print(f"\t{i * m}", end="")
    print()
