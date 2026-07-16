from collections import deque
grid = [[0,0,0],[1,1,0],[1,1,0]]

def shortest_path_matrix(grid):
    if grid[0][0] == 1:
        return -1
    row = len(grid)
    col = len(grid[0])

    visited = [[0 for _ in range(col)] for _ in range(row) ]

    queue = deque([])
    queue.append((0,0,1))
    visited[0][0] = 1

    directions = [(1,1), (-1, -1), (-1, 1), (1, -1), (1,0), (-1,0), (0,1), (0, -1)]

    while queue:
        u,v,d = queue.popleft()
        if u == row-1 and v == col-1:
            return d

        for dr, dc in directions:
            nr = dr + u
            nc = dc + v
            if nr>=0 and nr<row and nc>=0 and nc<col:
                if visited[nr][nc] == 0 and grid[nr][nc] == 0:
                    visited[nr][nc] = 1
                    queue.append((nr, nc, d+1))
    
    return -1

print(shortest_path_matrix(grid))
