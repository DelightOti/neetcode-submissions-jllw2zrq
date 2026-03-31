class Solution:
    def isValid(self, s: str) -> bool:
        
        '''
        create a stack
        create a dictionary to store the opening and closing brackets

        treat string as char array
        iterate over string
            if character is an opening bracket
                push it to the stack
            if it is a closing bracket
                if stack is empty
                    return false
                check if it is the correct closing paragraph
                    if not return False
            increment to next char
        return True if stack is empty
        '''

        stack=[]
        my_dict={'(':')',"{":"}","[":"]"}

        for char in s:
            if char in my_dict:
                stack.append(char)
            else:
                if not stack:
                    return False
                if char != my_dict[stack[-1]]:
                    return False
                
                stack.pop()
        return len(stack)==0