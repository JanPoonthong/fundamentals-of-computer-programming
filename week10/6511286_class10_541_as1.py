RESULT = []


def matrixMultiplication(mat1, mat2):
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                RESULT[i][j] += mat1[i][k] * mat2[k][j]

    for i in RESULT:
        print(i)


first_matrix = []
a = int(input("Enter for a first matrix size: "))
b = int(input("Enter for a second matrix size: "))

for i in range(a):
    first_matrix.append([])
    RESULT.append([])
    for j in range(a):
        first_matrix[i].append(
            int(input(f"Enter a matrix row for {i} column {j}: "))
        )
        RESULT[i].append(0)


print("")

second_matrix = []
for i in range(b):
    second_matrix.append([])
    RESULT.append([])
    for j in range(b):
        second_matrix[i].append(
            int(input(f"Enter a matrix row for {i} column {j}: "))
        )
        RESULT[i].append(0)

matrixMultiplication(first_matrix, second_matrix)
