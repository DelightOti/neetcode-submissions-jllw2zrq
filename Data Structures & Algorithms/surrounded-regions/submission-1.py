class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        # if its on the border meaning either if len(grid) = row or len(grid[0]) = col or if row = 0 or col = 0

        rows = len(board)
        cols = len(board[0])

        def dfs(row, col):

            # if on border return
            if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != 'O':
                return 
            
            # else change to X
            board[row][col] = '#'

            # call in all directions

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols - 1)
        
        for col in range(cols):
            dfs(0, col)
            dfs(rows - 1, col)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "#":
                    board[row][col] = "O" 