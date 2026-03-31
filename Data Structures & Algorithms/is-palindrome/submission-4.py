class Solution:
    def isPalindrome(self, s: str) -> bool:

        '''
        remove spaces in string

        set a pointer at start
        set a pointer at last character

        while left < right:
            while left pointer is not a character
                move by 1
            while right pointer is not a character
                move by 1
            
            if left != right
                return False
        return True
        '''

        s = s.replace(" ","").lower()


        left = 0
        right = len(s)-1

        while left < right:
            while left < right and s[left].isalnum() != True:
                left+=1
            
            while left < right and s[right].isalnum() != True:
                right-=1
            
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1

        return True