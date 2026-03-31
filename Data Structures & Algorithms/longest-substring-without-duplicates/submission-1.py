class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        '''
        Understanding: returning length of longest substring without duplicate characters

        Plan:

        use a set to store characters seen
        start two pointers at first index (left=0,right=0)
        iterate over the string (while right<len(string))
            if character not in set:
                add it to set
                increment right
            else character in set:
                move left up by 1
        return length of set
        '''

        my_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            # If character is a duplicate, shrink left pointer
            while s[right] in my_set:
                my_set.remove(s[left])
                left += 1

            # Add current character
            my_set.add(s[right])

            # Update max length
            max_len = max(max_len, right - left + 1)

        return max_len
