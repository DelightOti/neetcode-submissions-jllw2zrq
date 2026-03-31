class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        '''
        sort the array so i can use forward backward pointer technique

        left=1
        right=len(array)-1

        iterate over the array using enumerate
            if a and left are same:
                skip to next iteration

            sum = value at start +value at left + value at right

            if sum is too big
                shrink right
            
            if sum is too small
                move left up
            
            else
                append all three outputs to list
                move left up 1
                move right up 1
                check for left ad right ptr duplicate
        '''

        nums.sort()
        res= []

        for index,number in enumerate(nums):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            
            left= index+1
            right= len(nums) - 1
            
            while left<right:
                sum= number + nums[left] + nums[right]

                if sum > 0:
                    right-=1
                elif sum < 0:
                    left+=1
                else:
                    res.append([number, nums[left], nums[right]])
                    left+=1
                    right-=1

                    while left<right and nums[left] == nums[left-1]:
                        left+=1
                    while left<right and nums[right] == nums[right+1]:
                        right-=1
        return res
