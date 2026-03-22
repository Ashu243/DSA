matrix = [[1,1,1],[1,0,1],[1,1,1]]

rows = len(matrix)
cols = len(matrix[0])

rows_set = set()
cols_set = set()

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 0:
            rows_set.add(i)
            cols_set.add(j)

for i in range(rows):
    for j in range(cols):
        if i in rows_set or j in cols_set:
            matrix[i][j] = 0
 
# print(rows_set, cols_set)
print(matrix)