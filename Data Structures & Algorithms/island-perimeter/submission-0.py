class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def dfs(i, j):

            # base case is boundaries plus when it is in water
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 1
            
            # IF IN SET
            if (i,j) in visit:
                return 0

            visit.add((i,j))
            # call function on all direction

            perim = dfs(i+1, j) + dfs(i, j+1) + dfs(i, j-1) + dfs(i-1, j)

            return perim
        
        # start on land
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i, j)
        