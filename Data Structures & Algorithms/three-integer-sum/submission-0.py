class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        '''
        Plan:
        sort the array
        create res list to be returned

        iterate from i up until len(nums)i-2
            if first element is a duplicate
                skip
            l=i+1
            r=len(nums)-1
            
            while l<r:
                sum=nums[i]+nums[l]+nums[r]
                if s<0:
                    l+=1
                elif s>0:
                    r-=1
                else s=0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r+=1
                    while l<r and nums[l] is same as previous
                        l=l+1
                    while l<r and nums[r] is same as previous
                        r=r-1
        return res                     
        '''
        res=[]
        nums.sort()
        n=len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res