class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        '''
        plan: 
        create list
        fix i 
            check for duplicates
        fix j (j=i+1)
            check for duplicates

        left= j+1
        right=len(nums)-1
        while left<right:
            sum= i+j+value at left plus value at right

            if sum>target:
                decrease right
            if sorm < target:
                increase right
            else:
                add sum to a list
                check for duplicates left
                check for duplicates right
        return list
        '''

        nums.sort()
        res = []
        n = len(nums)-1 

        for i, num in enumerate(nums):
            if i>0 and num == nums[i-1]:
                continue
            
            for j in range(i+1, n):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                
                left = j+1
                right = n

                while left < right:
                    sum = num + nums[j] + nums[left] + nums[right]

                    if sum > target:
                        right-=1
                    elif sum < target:
                        left+=1
                    else:
                        res.append([num,nums[j],nums[left],nums[right]])
                        left+=1
                        right-=1

                        while left<right and nums[left] == nums[left-1]:
                            left+=1
                        while left<right and nums[right] == nums[right+1]:
                            right-=1
        return res