 
def nqueens(n):
    ans = []
    board = ['.'*n for _ in range(n)]

    def is_safe(col, row, board, n):
        duprow = row
        dupcol = col

        while row>=0 and col >= 0:
            if board[row][col] == 'Q':
                return False
            row -= 1
            col -=1

        row = duprow
        col = dupcol

        while col>=0:
            if board[row][col] == 'Q':
                return False
            col -= 1

        row = duprow
        col = dupcol
        
        while row<n and col>=0:
            if board[row][col] == 'Q':
                return False
            row += 1
            col -= 1
        
        return True 

    def solve(board, col, n, ans):
        if col == n:
            ans.append(list(board))
            return
        
        for row in range(n):
            if is_safe(col, row, board, n):
                board[row] = board[row][:col] + "Q" + board[row][col+1:]
                solve(board, col+1, n, ans)

                board[row] = board[row][:col] + "." + board[row][col+1:]

    solve(board, 0, n, ans)
    return ans

print(nqueens(4))




