class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        '''
        growing sliding window

        Plan:

        Create a variable left asd set it to zero
        Maximum to zero

        iterate over array using a right pointer and from the second value
            if right is greater than left value:
                profit= compute right value - left value
                Maximum is the max between profit and maximum
            else:
                # RIGHT ISNT GREATER
                left = right
        '''

        left=0
        maximum=0

        for right in range(1,len(prices)):
            
            if prices[right]>prices[left]:
                profit= prices[right]-prices[left]
                maximum=max(maximum,profit)
            
            else:
                left = right
        return maximum