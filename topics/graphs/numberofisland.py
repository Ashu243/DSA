from collections import deque
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
def islands(grid):
    row = len(grid)
    col = len(grid[0])
    queue = deque([])
    visited = [[0 for _ in range(col)] for _ in range(row)]
    result = 0
    def bfs(i, j):
        queue.append((i,j))
        directions = [(1,0), (-1,0), (0,1), (0, -1)]

        while queue:
            u, v = queue.popleft()

            for dr, dc in directions:
                nr = dr+u
                nc = dc+v
                if nr >= 0 and nr < row and nc >= 0 and nc <col:
                    if grid[nr][nc] == "1" and visited[nr][nc] == 0:
                        visited[nr][nc] = 1
                        queue.append((nr, nc))

    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1" and visited[i][j] == 0 :
                result += 1
                bfs(i, j)

    
    return result

print(islands(grid))
