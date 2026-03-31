class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        '''
        start a pointer at the first index
        create a set to store seen characters
        create a count variable to keep count of longest substring

        iterate over the string:
            if right is not in the set:
                add right to set
                increment count by 1
            else:
                # right is in the set
                move left by 1 to shrink the window
        return count
        '''    

        left = 0
        seen= set()
        count = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            
            seen.add(s[right])
            count= max(count, (right-left+1))
        return count

        
