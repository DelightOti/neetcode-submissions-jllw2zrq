class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        '''
        Understanding: find the longest substring

        Plan:
        start two pointers at first character
        use a dictionary to store strings already seen??
        move the pointers over the string
        if the pointer comes across a letter already in the sequence
        move the back pointer up 
        else
        keep moving the forward pointer
        return length of string
        '''

        my_dict={}
        left=0
        max_len=0

        for right in range(len(s)):
            char=s[right]
            if s[right] in my_dict and my_dict[char]>=left:
                left=my_dict[char]+1
        
            my_dict[char] = right    

            max_len = max(max_len, right - left + 1)
        
        return max_len
