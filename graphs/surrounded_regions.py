from collections import deque
board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]]


def surrounded_regions(board):
    row = len(board)
    col = len(board[0])
    visited = [[0 for _ in range(col)] for _ in range(row) ]

    queue = deque([])

    for i in range(row):
        for j in range(col):
            if i == 0 or i == row-1 or j == 0 or j == col-1:
                if board[i][j] == 'O':
                    visited[i][j] = 1
                    queue.append((i, j))

    directions = [(1,0), (-1, 0), (0,1), (0, -1)]

    while queue:
        u, v = queue.popleft()

        for dr, dc in directions:
            nr = dr + u
            nc = dc + v

            # valid 
            if nr >=0 and nr < row and nc >= 0 and nc < col:
                if board[nr][nc] == "O" and visited[nr][nc] == 0:
                    queue.append((nr, nc))
                    visited[nr][nc] = 1


    for i in range(row):
        for j in range(col):
            if visited[i][j] == 0 and board[i][j] == "O":
                board[i][j] = "X"
    
    return board


print(surrounded_regions(board))