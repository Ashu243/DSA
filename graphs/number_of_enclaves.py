from collections import deque
grid = [
    [0,0,0,0],
    [1,0,1,0],
    [0,1,1,0],
    [0,0,0,0]]


def enclaves(grid):
    row = len(grid)
    col = len(grid[0])

    queue = deque([])
    visited = [[0 for _ in range(col)] for _ in range(row)]

    for i in range(row):
        for j in range(col):
            if i == 0 or i == row-1 or j == 0 or j == col-1:
                if grid[i][j] == 1:
                    queue.append((i, j))
                    visited[i][j] = 1

    directions = [(1,0), (-1,0), (0, 1), (0, -1)]
    while queue:
        u, v = queue.popleft()

        for dr, dc in directions:
            nr = dr+u
            nc = dc + v

            if nr >= 0 and nr < row and nc >= 0 and nc < col:
                if grid[nr][nc] == 1 and visited[nr][nc] == 0:
                    queue.append((nr, nc))
                    visited[nr][nc] = 1
    
    count = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1 and visited[i][j] == 0:
                count += 1
    
    return count

print(enclaves(grid))
