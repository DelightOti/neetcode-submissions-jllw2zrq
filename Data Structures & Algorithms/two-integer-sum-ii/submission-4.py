class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        '''
        forward-backward two pointer technique

        Plan:

        set left ptr to 0
        set right ptr to last value

        while left<right:
            sum=left value plus right value
            if sum is too big:
                decrement it by moving right side down
            if sum is too small:
                increment by moving left side up
            else:
                return list of values
        '''

        left=0
        right=len(numbers)-1

        while left<right:
            sum=numbers[left]+numbers[right]

            if sum > target:
                right-=1
            
            elif sum < target:
                left+=1
            
            else:
                return [left+1, right+1]



