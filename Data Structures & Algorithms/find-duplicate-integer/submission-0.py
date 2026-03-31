class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        '''
        create a dictionary to store the number and count
        iterate over the array nums
            store the number and the count in the dictionary
        return the key with the greatest value
        '''

        my_dict={}

        for i in nums:
            if i in my_dict:
                return i
            else:
                my_dict[i]=1
        
        return -1
        