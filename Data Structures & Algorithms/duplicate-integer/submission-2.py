class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        '''
        create a dictionary to store seen values
        iterate over the integer array
        if the number exists in the dictionary
            increment by 1
        else
            add the number to the dictionary and set value to 1
        '''

        my_dict={}
        for i in nums:
            if i in my_dict:
                return True
            else:
                my_dict[i]=1
        return False