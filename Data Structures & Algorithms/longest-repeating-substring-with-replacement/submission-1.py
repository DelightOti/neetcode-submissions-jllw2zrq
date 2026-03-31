class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        '''
        Understanding: perform k changes to letters in s to return length of longest substring

        Plan:
        use sliding window technique
        start left pointer at starting character
        start right pointer at starting character
        create a hash map my_dict to store count of characters
        result to store window size

        use a while loop - while right < length of string
        if character not in my_dict
            add character to my_dict and set count to 1 
        else (character in my dict)
            increment count by 1
        check if (windowsize-max(between characters in dictionary)) <= k:
            if True good
        else:
            increment left by 1 to adjust the window
            decrement count in dict
        increment right by 1
        increment result by 1
        '''

        left=0
        right=0
        my_dict={}
        res=1

        while right<len(s):
            # build hash map
            if s[right] not in my_dict:
                my_dict[s[right]]=1
            else:
                my_dict[s[right]]+=1

            # window size
            window= right-left+1

            # max-freq= max(my_dict.values())
            max_freq=max(my_dict.values())
    
            if window-max_freq>k:
                # decrement count in hash map
                my_dict[s[left]]-=1
                # increase pointer
                left+=1
            
            res=max(res,right-left+1)
            right+=1
        return res
