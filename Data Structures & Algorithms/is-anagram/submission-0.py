class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        '''
        understanding: im checking if two strings are anagrams and basically
        what that means is do the contain the exact same character

        Plan:
        sort both of the strings
        if s is equal to t 
            return True bc they are the same
        else 
            return false
        '''

        news=''.join(sorted(s))
        newt=''.join(sorted(t))

        if news == newt:
            return True
        else:
            return False
