number = int(input("Enter 5-digit number: "))
count = 0
cal_number = number

# Count digit
while cal_number != 0:
    cal_number //= 10
    count += 1

if count <= 4:
    print("Wrong Input. Try Again")
    exit(1)

ten_thousand = number // 10000
thousand = (number // 1000) % 10
hundred = (number % 1000) // 100
ten = (number % 100) // 10
unit = number % 10

sum_of_four_num = ten_thousand + thousand + ten + unit

if hundred > sum_of_four_num:
    swap_num = (
        str(unit) + str(thousand) + str(hundred) + str(ten) + str(ten_thousand)
    )
elif hundred == sum_of_four_num:
    print(f"The output is {number}")
    exit()
else:
    swap_num = (
        str(ten_thousand) + str(ten) + str(hundred) + str(thousand) + str(unit)
    )

print(f"The output is {swap_num}")
