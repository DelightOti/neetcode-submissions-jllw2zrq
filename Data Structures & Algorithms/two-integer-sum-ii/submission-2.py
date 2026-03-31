class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        '''
        set left ptr=0
        set right pointer to last index
        iterate over the array left<right
            value=value at left + value at right
            if value == target
                return the left and right 1 indexed at a list
            elif value<target:
                move left up 1
            else value>target:
                move right down by 1
        '''

        left=0
        right=len(numbers)-1

        while left<right:
            value=numbers[left]+numbers[right]
            if value==target:
                return [left+1,right+1]
            elif value<target:
                left+=1
            else:
                right-=1


