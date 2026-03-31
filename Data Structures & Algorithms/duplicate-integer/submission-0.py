class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        '''
        Plan: Create a dictionary or a tuple to store the key value pairs
        and if a value ever has two then stop counting and return true
        else if i make it to the en of the list and no value changes to two 
        return false

        Pseudocode:
        Create a dictionary my_dict

        iterate over nums using a for loop
            if nums[i] exists in dictionary
                return true
            else
                for every new nums[i] append it to my_dict
        return false
        '''

        # Create a dictionary my_dict
        my_dict={}

        # iterate over nums using a for loop
        for i in range(0,len(nums)):
        #if nums[i] exists in dictionary
            if nums[i] in my_dict:
        #return true
                return True
        #else
            else:
        #for every new nums[i] append it to my_dict
                my_dict[nums[i]]=1
        # return false
        return False