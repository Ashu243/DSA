from collections import deque

grid = [[2,1,1],[1,1,0],[0,1,1]]


def rotten_oranges(grid):
    row = len(grid)
    col = len(grid[0])

    queue = deque([])
    fresh_count = 0

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 2:
                queue.append((i,j))
            elif grid[i][j] == 1:
                fresh_count += 1 

    directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
    minutes = 0


    while queue and fresh_count > 0:

        for _ in range(len(queue)):
            i, j = queue.popleft()

            for dr, dc in directions:
                nr = dr+i
                nc = dc+j

                # valid
                if nr>=0 and nr < row and nc >= 0 and nc < col:
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
            
        minutes += 1

        
    return minutes if fresh_count == 0 else -1

print(rotten_oranges(grid))