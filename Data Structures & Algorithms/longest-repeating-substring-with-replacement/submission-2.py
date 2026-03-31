class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        '''
        create cariable for frequency map 
        set left to zero
        set res to zero
        set max_freq to zero

        iterate over string using right:
            if letter not in map
                add it
            else
                increment by 1

            windowize= r - l + 1
            
            if windowsize - maxfreq > k:
                decrement left from map 
                left += 1
            else:
                res is max between res and windowsize
        return res
        '''
        count = {}
        res = 0
        left = 0
        max_freq = 0

        for right in range(len(s)):
            count[s[right]]= count.get(s[right],0)+1

            max_freq = max(count.values())

            window_size = (right - left) + 1

            if window_size - max_freq > k:
                count[s[left]]-=1
                left+=1
            else:
                res = max(res, window_size) 
        return res