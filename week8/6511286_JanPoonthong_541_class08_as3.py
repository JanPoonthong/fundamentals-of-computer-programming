# 3. Write  a  Python  code  to  create  a  list  (and  print  all  elements  in  the  list as  an output) by concatenating each individual string (a single character) inputwith digitsranging from 1 to n. For the output, a character must be capitalized.
user_input_char = input("Input: ").split(" ")
user_input_int = int(input("Enter a value of n: "))

for i in user_input_char:
    for j in range(1, user_input_int + 1):
        print(f"{i.upper()}{j}", end=" ")
