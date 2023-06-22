# 4. Based  on  assignment  3,  if an  associated  digit  is an  odd  number,  a character must be a lowercase letter.
user_input_char = input("Input: ").split(" ")
user_input_int = int(input("Enter a value of n: "))

for i in user_input_char:
    for j in range(1, user_input_int + 1):
        if j % 2 == 0:
            print(f"{i.upper()}{j}", end=" ")
        else:
            print(f"{i.lower()}{j}", end=" ")
