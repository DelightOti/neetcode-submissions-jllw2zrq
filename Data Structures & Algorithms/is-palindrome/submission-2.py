class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        '''
        Plan:
        remove all spaces using the remove function
        ptr2=len(s)-1

        iterate over s using a while loop
            if i(ptr1) is not a letter:
                move i + 1
            if ptr2 is not a letter:
                move ptr2-1
            check if i is a letter and p is a leter and if i not equal to p
                return False
            
            increment i
            decrement ptr2
        return True //cus by the time u get here its a palindrme
            
        '''
        # remove all spaces using the remove function
        new_s=s.replace(" ","")
        # ptr2=len(s)-1
        ptr2=len(new_s)-1
        i=0

        # iterate over new_s using a while loop
        while i<ptr2:
        #     if i(ptr1) is not a letter:
            if not new_s[i].isalnum():
        #         move i + 1
                i+=1
                continue
        #     if ptr2 is not a letter:
            if not new_s[ptr2].isalnum():
        #         move ptr2-1
                ptr2-=1
                continue
        #     check if i is a letter and p is a leter and if i not equal to p
            if new_s[i].lower() != new_s[ptr2].lower():
                return False
            
        #     increment i
            i+=1
        #     decrement ptr2
            ptr2-=1
        # return True //cus by the time u get here its a palindrme
        return True
            