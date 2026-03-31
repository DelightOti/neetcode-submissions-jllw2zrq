class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        '''
        Plan:
        sort s
        sort t
        if sorted_s = sorted_t:
            return True
        return False

        make a dictionary
        iterate over s
            store thr values of s in the dictionary with their count
        iterave over t
            store the valeus of t in the dictionary with their conut
        check is the two dictionairies are the same
            return True
        return False
        '''

        sorted_s=sorted(s)
        sorted_t=sorted(t)
        if sorted_s==sorted_t:
            return True
        return False