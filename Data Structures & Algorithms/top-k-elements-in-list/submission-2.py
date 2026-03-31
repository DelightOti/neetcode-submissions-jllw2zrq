class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        '''
        K represents the top elements that appear frequently so if k is 2
        return a list with the top two elements

        Plan:
        Create a dictionary my_dict to store number and count

        Iterate over nums list and create the dictionary

        dictionary is created in ascending order so 
        sort the dictionary by values so from smaller to higher numbers
        and then reverse it 

        create a list to be returned

        iterate over dictionary until length of list<2
            append dictionary key to list
        '''
        # Create a dictionary my_dict to store number and count
        my_dict={}

        # Iterate over nums list and create the dictionary
        for i in nums:
            if i in my_dict:
                my_dict[i]+=1
            else:
                my_dict[i]=1

        # dictionary is created in ascending order so 
        # sort the dictionary by values so from smaller to higher numbers
        # and then reverse it 
        sorted_D=list(sorted(my_dict.items(), key=lambda x:x[1], reverse=True))

        # create a list to be returned
        tbr=[]

        # iterate over dictionary until length of list<2
        while len(tbr)<k:
        #     append greatest dictionary key to list
            tbr.append(sorted_D[len(tbr)][0])
        return tbr