class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        '''
        So the formula is area= minimum of (left and right) times (distance between left and right)

        Plan:

        Set right pointer (ptr2) = len(height) - 1
        Set Area = 0
        
        Iterate over array while left is less than right:
            calculate array to start using the area formula
            if area is greater than area
                set area to newarea
            
            Then move the minimum between the left and right pointer        
        '''

        right= len(heights)-1
        left=0
        Area = 0

        while left<right:
            newArea= min(heights[left],heights[right]) * (right-left)
            if newArea>Area:
                Area=newArea
            
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        
        return Area

