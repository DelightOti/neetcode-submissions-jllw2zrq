class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        '''
        Plan:
        set count=0
        use a set to store characters seen
        Start both pointers at the start

        while right < len(s):
            if right character in set:
                move left by 1
            else:
                count+=1
            move right by 1
        
        return count
        '''

        count=0
        my_set=set()
        left=0
        right=0

        while right<len(s):
            if s[right] in my_set:
                my_set.remove(s[left])
                left+=1
            else:
                my_set.add(s[right])
                count= max(count, right-left+1)
                right+=1
        
        return count
