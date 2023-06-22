user_number = int(input("Enter number of real numbers: "))
count = 0
number_list = []

while user_number > 0:
    count += 1
    number = float(input(f"Number#{count}: "))
    number_list.append(number)
    number_list.sort()
    user_number -= 1

print(f"The first highest number is {number_list[-1]}")
if not count == 1:
    print(f"The second highest number is {number_list[-2]}")
else:
    print("The is no second highest number")
