class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        '''
        understanding: returning the maximum profit of NeetCoin by going through an array
        and picking the best day in the future to sell it

        Plan:
        Use dynamic sliding window pattern

        Set maxprofit variable to 0
        set left to 0
        set right to left+1

        iterate over array using while loop(while right is less than len(prices))
            if array[left] < array[right]:
                profit=array[right]- array[left]
                if profit>max_profit:
                    update max_profit
            else
                if array[right] < array[left]:
                    left=right
            right+=1
        return maxprofit
        '''
        max_profit=0
        left=0
        right=left+1

        while right<len(prices):
            if prices[left] < prices[right]:
                profit=prices[right] - prices[left]
                if profit > max_profit:
                    max_profit = profit
            elif prices[right] < prices[left]:
                left = right
            right+=1
        return max_profit
                
