class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col, distance):

            if row < 0 or col < 0 or row >= rows or  col >= cols or grid[row][col] == -1 or grid[row][col] < distance:
                return
            
            grid[row][col] = distance

            dfs(row + 1, col, distance + 1)
            dfs(row - 1, col, distance + 1)
            dfs(row, col + 1, distance + 1)
            dfs(row, col - 1, distance + 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    dfs(row, col, 0)
        