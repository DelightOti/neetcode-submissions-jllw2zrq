class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        '''
        Plan:

        for each value in strs, 
        sort it
        if it exists in the dict:
            append the word to it
        else
            create a new key and append the word o it
        return a list with the values
        '''
        res= defaultdict(list)

        for s in strs:
            sorteds=''.join(sorted(s))
            if sorteds in res:
                res[sorteds].append(s)
            else:
                res[sorteds].append(s)
        return list(res.values())   