class Solution:
    def validPalindrome(self, s: str) -> bool:

        '''
        Plan:

        set left to zero
        set right to last character in string

        if original string is equal to reverse of original stirng 
            return true

        while left < right:
            if char at left == char at right:
                move left by 1 
                right by 1
            
            if char at left != char at right:
                check left:
                    remove  left and check if new string after removing is equal tp reverse
                    if equal:
                        return true
                
                check right:
                    remove right from original check if new string is equal o reverse
                    if equal:
                        return true
        return false
        '''
        
        l = 0
        r = len(s) - 1

        rev_s = s[::-1]
        if s == rev_s:
            return True

        while l < r:
            if s[l] != s[r]:
                # check left, right by removing using splice
                L_Skip, R_Skip = s[l+1 : r+1] , s[l : r]
                rev_L = L_Skip[::-1]
                rev_R = R_Skip[::-1]

                if L_Skip == rev_L or R_Skip == rev_R:
                    return True
                else:
                    return False
            
            l+=1
            r-=1

        return False

