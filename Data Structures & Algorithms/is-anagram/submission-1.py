class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        '''
        Plan:

        sort s and sort t
        if s == t:
            return True
        return False
        '''

        sorteds= ''.join(sorted(s))
        sortedt=''.join(sorted(t))

        if sorteds == sortedt:
            return True
        else:
            return False