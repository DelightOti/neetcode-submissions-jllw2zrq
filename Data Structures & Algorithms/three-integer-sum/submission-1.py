class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        '''
        Understanding: No duplicates in outputs

        Plan:

        sort the list
        create list tbr 

        Iterate over sorted nums list using a while loop
        have j be i+1
        
        since nums[i] + nums[j] + nums[k] == 0

        s= nums[i]+nums[j]

        k= difference between 0 and s so 0-s

        check if k exists in the nums array if it doesnt scrap the list and 
        iterate i by 1, and j by 1        

        else if it does
        insert i,j,j into same index at tbr
        '''

        nums=sorted(nums)
        tbr=set()
        i=0

        while i<(len(nums)-2):
            j=i+1
            
            while j<len(nums)-1:
                s=nums[i]+nums[j]
                k=0-s

                for ptr2 in range(j+1,len(nums)):
                    if nums[ptr2] == k:
                        triplet=(nums[i],nums[j],nums[ptr2])
                        tbr.add(triplet)
                j+=1
            i+=1
        # since it is a set for t in set change back to list
        result = []
        for t in tbr:
            converted = list(t)   # convert tuple → list
            result.append(converted)
        return result