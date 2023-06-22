birth_day = input("Assume that your date of birth: ")
year = int(input("Enter your year of birth (A.D.): "))

age = (2021 - year) + 1

for i in range(2021, year - 1, -1):
    print(f"By {birth_day} {i}, you are {age} year old")
    age -= 1
