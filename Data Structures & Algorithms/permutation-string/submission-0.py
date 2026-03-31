class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        '''
        Build a dictionary for string1 with all the characters and their counts call it need
        Build a dictionary for string2 but leave it empty

        create like a valid checker
        create a left pointer for string 2
        iterate over strgin 2 using a right pointer:
            assign current rght to a character
            if character in need:
                add it to window
                if window equal to need:
                    increment valid to know that for that letter it is good

            if window too large (right-left +1 > (length of s1)):
                set d o character left
                if character in need:
                    if window[d] is same as nned[d]
                        decrement valid
                    decrement window
                increment left
            
             at the end if valid=length of s1:
                 return ture
        else
        return false
        '''

        s1_dict={}
        for i in s1:
            if i in s1_dict:
                s1_dict[i]+=1
            else:
                s1_dict[i]=1

        s2_dict={}
        valid=0
        left=0

        for right in range(len(s2)):
            c=s2[right]

            if c in s1_dict:
                s2_dict[c] = s2_dict.get(c, 0) + 1
                if s2_dict[c] == s1_dict[c]:
                    valid += 1
            
            window=(right-left)+1
            if window>len(s1):
                d=s2[left]
                if d in s1_dict:
                    if s2_dict[d]==s1_dict[d]:
                        valid-=1
                    s2_dict[d]-=1
                left+=1

            if valid==len(s1_dict):
                return True
        return False