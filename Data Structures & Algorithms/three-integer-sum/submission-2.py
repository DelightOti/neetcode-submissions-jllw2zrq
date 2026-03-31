class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        '''
        Understanding: No duplicates in outputs

        Plan:
        sort the list
        create list to be returned

        iterate over the sorted list using a while loop
            if i > 0 and i is the same as the one in the index before:
                continue to next iteration
            
            l=i+1
            r=len(nums)-1

            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if s>0:
                    r-=1
                elif s<0:
                    l+=1
                else:
                    tbr.append(nums[i],nums[l],nums[r])
                    l+=1
                    r-=1
                    check for left ptr duplicate
                    check for right ptr duplicate
        return list                
        '''

        # sort the list
        nums=sorted(nums)
        # create list to be returned
        tbr=[]
        i=0
        # iterate over the sorted list using a while loop
        while i<len(nums)-2:
        #     if i > 0 and i is the same as the one in the index before:
            if i>0 and nums[i]==nums[i-1]:
                i+=1
        #         continue to next iteration
                continue
        #     l=i+1
            l=i+1
            r=len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if s>0:
                    r-=1
                elif s<0:
                    l+=1
                else:
                    tbr.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
            i+=1
        return tbr

