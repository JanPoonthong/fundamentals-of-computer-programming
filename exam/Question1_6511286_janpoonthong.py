volume = float(input("Enter the volume of the crude oil in liter(s): "))
answer = ((97.59 * volume) / 158.98) * 36.56
print(
    f"The {volume} Liter(s) crude oil will cost {round(answer, 2)} in Thai Bath(s)."
)
