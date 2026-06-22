from collections import deque
grid = [
    ['L', 'L', 'W', 'L', 'L'],
    ['L', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'L'],
    ['L', 'L', 'W', 'L', 'L']
]

def distinct_islands(grid):
    row = len(grid)
    col = len(grid[0])

    visited = [[0 for _ in range(col)] for _ in range(row)]

    resultSet = set()

    def bfs(i, j):
        queue = deque([])
        queue.append((i, j))
        directions = [(1,0), (-1, 0), (0,1), (0, -1)]
        structure = []

        while queue:
            u, v = queue.popleft()
            
            for dr, dc in directions:
                nr = dr+u
                nc = dc+v
                if nr >=0 and nr<row and nc>=0 and nc<col:
                    if grid[nr][nc] == "L" and visited[nr][nc] == 0:
                        row_diff = nr-i
                        col_diff = nc-j
                        structure.append((row_diff, col_diff))
                        visited[nr][nc] = 1
                        queue.append((nr, nc))
        resultSet.add(tuple(structure))

    for i in range(row):
        for j in range(col):
            if grid[i][j] == "L" and visited[i][j] == 0:
                visited[i][j] = 1
                bfs(i, j)

    return len(resultSet)

print(distinct_islands(grid))