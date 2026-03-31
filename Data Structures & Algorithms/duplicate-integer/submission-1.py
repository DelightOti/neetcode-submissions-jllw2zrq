class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        '''
        Plan:

        create an empty dict my_dict

        iterate over nums:
            if a value already exists in my_dict then
                increment the count by 1
            else if it doesnt exist
                create a new key and set value to 1
            if value of my dict is 2:
                return True
        
        return False
        '''

        my_dict={}

        for i in nums:
            if i in my_dict:
                my_dict[i]+=1
            else:
                my_dict[i]=1
            
            if my_dict[i]==2:
                return True
        return False

