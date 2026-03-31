class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        '''
        Understanding: Given an array, return the k most frequent elements with
        in the arrray (k controls how many elements you are returning)

        Plan:
        create a dictionary

        build the dictionary with the key and their values
        Iterate over nums
            if item at index does not exist:
                create a new key in dictionary and set count to 1
            else if it already exists
                increment the count of value to 1
        
        create list to be returned
        while list is less than k:
            go thru dictionary and append the biggest number 
            then next biggest
        return list
        '''
        # create a dictionary
        my_dict={}

        # build the dictionary with the key and their values
        # Iterate over nums
        for i in nums:
        #     if item at index does not exist:
            if i in my_dict:
                my_dict[i]+=1
            else:
                my_dict[i]=1
       
        
        # create list to be returned
        tbr=[]
        # sort the dictionary
        sorteddict=sorted(my_dict.items(), key=lambda x:x[1], reverse=True)
        # while length of list is less than k
        while len(tbr)<k:
            # append dictionaty values to list
            tbr.append(sorteddict[len(tbr)][0])
        return tbr
            
