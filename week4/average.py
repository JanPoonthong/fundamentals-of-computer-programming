number = int(input("How many numbers?: "))
count = 0
sum_number_positive = 0
sum_number_negative = 0
sum_of_user_number = 0

while number > 0:
    count += 1
    user_number = int(input(f"Number#{count}: "))
    if user_number < 0:  # check negative
        sum_number_negative += user_number
    else:
        sum_number_positive += user_number
    number -= 1
    sum_of_user_number += user_number

average = sum_of_user_number / count
print(f"The average of these number is {average}")
print(f"The sum of all positive integers is {sum_number_positive}")
print(f"The sum of all negative integers is {sum_number_negative}")
