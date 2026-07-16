matrix = [[1,2,3],[4,5,6],[7,8,9]]

rows = len(matrix)
cols = len(matrix[0])
result = [[0]*cols for i in range(rows)]

# for i in range(rows):
#     for j in range(cols):
#         index = (rows-1)-i
#         result[j][index] = matrix[i][j]

# print(result)

for i in range(rows):
    for j in range(i, cols):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for row in matrix:
    row.reverse()

print(matrix)

