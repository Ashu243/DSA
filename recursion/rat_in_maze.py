maze = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]

def rat_maze(maze):
    n = len(maze)
    visited = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
    result = []

    def solve(maze, row, col, ans, n):
        if row == n-1 and col == n-1:
            result.append(ans)
            return 
        
        visited[row][col] = 1
        # down
        if row+1 < n and maze[row+1][col] == 1 and visited[row+1][col] == 0:
            visited[row][col] = 1
            solve(maze, row+1, col, ans+'D', n)

        # left
        if col-1 >= 0 and maze[row][col-1] == 1 and visited[row][col-1] == 0:
            visited[row][col] = 1
            solve(maze, row, col-1, ans+'L', n)

        # right
        if col+1 < n and maze[row][col+1] == 1 and visited[row][col+1] == 0:
            visited[row][col] = 1
            solve(maze, row, col+1, ans+'R', n)

        # up
        if row-1 >= 0 and maze[row-1][col] == 1 and visited[row-1][col] == 0:
            visited[row][col] = 1
            solve(maze, row-1, col,  ans+'U', n)
        
        visited[row][col] = 0

    solve(maze, 0, 0, '', n)
    return result

print(rat_maze(maze))