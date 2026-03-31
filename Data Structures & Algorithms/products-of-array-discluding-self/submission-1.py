class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        '''
        Let n = length of nums
        Create array prefix of size n
        Create array suffix of size n
        Create array res of size n

        # Build prefix products
        prefix[0] = 1
        for i from 1 to n-1:
            prefix[i] = prefix[i-1] * nums[i-1]

        # Build suffix products
        suffix[n-1] = 1
        for i from n-2 down to 0:
            suffix[i] = suffix[i+1] * nums[i+1]

        # Build result
        for i from 0 to n-1:
            res[i] = prefix[i] * suffix[i]

        return res
        '''
        n=len(nums)
        prefix=[1]*n
        suffix=[1]*n
        res=[1]*n

        prefix[0]=1  #nothing before 0 index
        for i in range(1, n):
            prefix[i]=prefix[i-1]*nums[i-1]
        
        suffix[n-1]=1 #nothing after end list
        for i in range(n-2, -1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]

        for i in range(n):
            res[i]=prefix[i] * suffix[i]
        
        return res