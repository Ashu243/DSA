matrix = [[2, 3, 5], [6, 4, 9], [1, 5, 9]]



rows = len(matrix)
columns = len(matrix[0])

print(f"{rows} rows and {columns} columns")

# sum = 0
# for i in range(rows):
#     for j in range(columns):
#         sum = sum + matrix[i][j]

# print(sum)


# upper traingle of matrix
# for i in range(rows):
#     for j in range(columns):
#         if j>=i:
#             print(matrix[i][j], end=" ")
#         else:
#             print("*", end=" ")
#     print()

# lower triangle of matrix
# for i in range(rows):
#     for j in range(columns):
#         if j<=i:
#             print(matrix[i][j], end=" ")
#         else:
#             print("*", end=" ")
#     print()

# printing only diagonals of matrix
# for i in range(rows):
#     for j in range(columns):
#         if j==i:
#             print(matrix[i][j], end=" ")
#         else:
#             print("*", end=" ")
#     print()


# for i in range(rows):
#     for j in range(columns):
#         if j+i == 2:
#             print(matrix[i][j], end=" ")
#         else:
#             print("*", end=" ")
#     print()


matrix2 = [[0]*rows for i in range(columns)]

for i in range(rows):
    for j in range(columns):
        matrix2[j][i] = matrix[i][j]

print(matrix)
print(matrix2)