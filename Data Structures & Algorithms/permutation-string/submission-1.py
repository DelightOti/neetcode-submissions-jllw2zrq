from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        '''
        create a hashmap of s1

        iterate over s2 using a slidin window of length s1
            if hashmap of window isnt equal to hashmap of s1:
                empty hashmap of window
                increment left by 1
            else:
                return True
        return False
        '''

        s1_count = Counter(s1)
        s2_count = {}

        left = 0

        for right in range(len(s2)):
            s2_count[s2[right]] = s2_count.get(s2[right], 0) + 1


            if right - left + 1 > len(s1):
                s2_count[s2[left]]-=1
                if s2_count[s2[left]] == 0:
                    del s2_count[s2[left]]
                left+=1

            if right - left + 1 == len(s1):
                if s2_count == s1_count:
                    return True
        return False
        
