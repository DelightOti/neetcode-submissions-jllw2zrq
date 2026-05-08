class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        '''
        
        set islands to 0

        make a dfs function(number):
            for each direction call the dfs fnction

        call it on a starting point where its 1
        '''

        islands = 0
        rows = len(grid)
        cols= len(grid[0])

        def dfs(row, col):

            # base case is when:
            # its water
            # its out of bounds on rows
            # out of bounds on cols
            if row >= rows or col >= cols or row < 0 or col < 0 or grid[row][col] == "0":
                return
            
            grid[row][col] = "0"

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands+=1 
        
        return islands