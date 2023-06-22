nums = input("Enter number(s) separated by space: ").split(" ")

int_nums = []
for number in nums:
    int_nums.append(int(number))

int_nums.sort()
del int_nums[0]
del int_nums[-1]

sum = 0
for number in int_nums:
    sum += int(number)

print(
    f"The average of number(s) in list excluding highest and lowest is {round(sum / len(int_nums), 2)}"
)

# 4 9 1 6 10
# 4 -10 1 3 1 9 2 100 20
