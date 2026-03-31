class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        '''
        maximum amount of water seems to be length times width
        length being height of smaller bar and width being distance between bar1 and bar2

        use forward backward technique and condition is to move the height with the smaller height
        
        return maximum amount of water

        Plan:
        create a variable maximum set it to zero

        start a pointer at beginning of the array
        start a pointer at the end of the array

        while left < right:
            width= right-left + 1
            height= smaller between left value and right value

            calculate left times right

            if it is greater than maximum:
                change value of maximum
            move the smaller pointer
                if right is smaller 
                    move it down
                if left is smaller move up
        '''

        maximum= 0

        left=0
        right= len(heights) - 1

        while left<right:
            width = right - left
            length = min(heights[right], heights[left])
            amount = width * length

            if amount > maximum:
                maximum = amount

            if heights[right] < heights[left]:
                right -=1
            else:
                left+=1
        return maximum 

