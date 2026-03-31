class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        '''
        make a new dictionary res

        iterate over the array
            sort the array to get my key
            if key is not in dict:
                add key to dict by create a new list
            else:
                add value to key in array
        '''

        res={}

        for i in strs:
            key="".join(sorted(i))
            if key not in res:
                res[key]=[]
            res[key].append(i)
        return list(res.values())