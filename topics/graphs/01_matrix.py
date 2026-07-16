from collections import deque
mat = [[0,0,0],[0,1,0],[1,1,1]]

# def matrix(mat):
#     row = len(mat)
#     col = len(mat[0])
#     visited = [[0 for _ in range(col)] for _ in range(row)]

#     queue = deque([])

#     for i in range(row):
#         for j in range(col):
#             if mat[i][j] == 0:
#                 queue.append((i,j,0))
#                 visited[i][j] = 1
    
#     directions = [(0,-1), (0,1), (1,0), (-1,0)]

#     while queue:
#         u,v,d = queue.popleft()

#         mat[u][v] = d

#         for x, y in directions:
#             nx = u + x
#             ny = v + y
#             if nx >= 0 and nx < row and ny >= 0 and ny < col:
#                 if visited[nx][ny] == 0:
#                     visited[nx][ny] = 1
#                     queue.append((nx, ny, d+1))
    
#     return mat

# print(matrix(mat))



def matrix(mat):
    row = len(mat)
    col = len(mat[0])

    visited = [[0 for _ in range(col)] for _ in range(row)]

    queue = deque([])

    for i in range(row):
        for j in range(col):
            if mat[i][j] == 0:
                queue.append((i,j,0))
                visited[i][j] = 1

    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    while queue:
        u,v,d = queue.popleft()

        mat[u][v] = d

        for dr, dc in directions:
            nr = dr+u
            nc = dc+v

            # valid direction
            if nr >= 0 and nr < row and nc >= 0 and nc < col:
                if visited[nr][nc] == 0:
                    queue.append((nr, nc, d+1))
                    visited[nr][nc] = 1

    return mat

print(matrix(mat))
