from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # use bfs bc i would need to start from rotten fruit and proceed outward

        # first make the queue

        queue = deque()
        fresh = 0
        rotten = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        
        # make the directions 
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        # iterate over the queue

        while fresh>0 and queue:

            length = len(queue)

            for i in range(length):
                row, col = queue.popleft()

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    if 0<= new_row < len(grid) and 0<= new_col < len(grid[0]) and grid[new_row][new_col] == 1:

                        grid[new_row][new_col] = 2
                        fresh -= 1
                        queue.append((new_row, new_col))
                  
            time+=1
        
        if fresh == 0:
            return time
        else:
            return -1



