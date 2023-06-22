num_a = int(input("First integer: "))
num_b = int(input("Second integer: "))

cal_a = num_a
cal_b = num_b

sum_num = 0

if cal_a > cal_b:
    while cal_b < cal_a:

        if not (cal_b % 3 == 0 and cal_b % 7 == 0):
            print(cal_b)

        sum_num += cal_b
        cal_b += 1

        if not ((sum_num) < (5 * num_a)):
            break
else:
    while cal_a < cal_b:

        if not (cal_a % 3 == 0 and cal_a % 7 == 0):
            print(cal_a)

        sum_num += cal_a
        cal_a += 1

        if not ((sum_num) < (5 * num_b)):
            break
