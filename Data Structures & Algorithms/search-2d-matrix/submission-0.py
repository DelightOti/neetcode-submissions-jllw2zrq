class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        '''
        understanding: returning true if a target exists in a matrix

        Plan:
        use the first column to check if the target is greater or less than 
        value at first row in first column
        if less i know it is in the one before
            
        if greater 
            check if target is less than value in the last column of the matrix
            if less just go back in that row until you find it
        '''
        m=len(matrix)
        n=len(matrix[0])

        r=0
        c=n-1

        while r < m and c >= 0:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True
        return False