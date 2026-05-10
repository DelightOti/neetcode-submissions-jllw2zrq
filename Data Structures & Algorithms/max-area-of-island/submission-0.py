class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        '''
        get rows
        get cols

        create dfs function(island):

            base case:
                if row < 0 or col < o0 or row > len(grid) or cols > len(grid[0] or the square isnt
                an island)
                    return
                
                count+=1

                dfs all directions
        
        call function on island
        '''

        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0

        def dfs(row, col):

            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            
            area = 1

            area += dfs(row+1, col)
            area += dfs(row-1, col)
            area += dfs(row, col+1)
            area += dfs(row, col-1)

            return area
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    current_area = dfs(row, col)
                    maxArea = max(current_area, maxArea)
        
        return maxArea
        