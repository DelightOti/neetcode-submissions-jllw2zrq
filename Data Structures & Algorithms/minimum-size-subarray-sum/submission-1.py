class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        '''
        Create window_length variable to zero
        Set left to zero
        Set sum to first value in arrray

        if sum == target:
            return 1

        iterate over nums using right starting from firs index:
            sum = sum += rigth value

            if sum > target:
                if window_size < window_length:
                    change window_length to window_size
                increase left by 1
            
            if sum == target:
                if window_size < window_length:
                    change window_length to window_size
        
        return window_length
        '''

        window_length = float("inf")
        left = 0
        sum = 0

        for right in range(len(nums)):
            sum += nums[right]

            while sum >= target:
                if right - left + 1 < window_length:
                    window_length = right - left + 1
                sum -= nums[left]
                left += 1
        
        return 0 if window_length == float('inf') else window_length
