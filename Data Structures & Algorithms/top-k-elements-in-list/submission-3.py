class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        '''
        returning a list with k most frequent elements in list

        Plan:
        Make the dictionary

        Reverse the dictionary starting from the largest values to the smallest values

        while length of string to be returned is less than k:
            put values ifrom mu reserved list inti the array and
        return result list
        '''

        my_dict={}

        for i in nums:
            if i in my_dict:
                my_dict[i]+=1
            else:
                my_dict[i]=1
        
        reverse_dict= sorted(my_dict.items(), key=lambda x:x[1], reverse=True)

        res=[]
        for i in range(k):
            res.append(reverse_dict[i][0])
        return res
