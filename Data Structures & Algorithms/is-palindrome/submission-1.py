class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        '''
        Plan:

        
        news= use funtion to remove spaces in string
        ptr1 starts at s[0]
        pr2 starts at s.length-1
        iterate over s by using the two pointer method
            if value at ptr1 and ptr2 are letters and if ptr1 != ptr2
                return False
        return True
        '''

        new_s=s.lower().replace(" ","")
        ptr2=len(new_s)-1
        i=0

        while i<ptr2:
            if not new_s[i].isalnum():
                i+=1
                continue
            if not new_s[ptr2].isalnum():
                ptr2-=1
                continue
            if new_s[i].isalnum() and new_s[ptr2].isalnum and new_s[i] != new_s[ptr2]:
                return False
            
            i+=1
            ptr2=ptr2-1
        return True

                