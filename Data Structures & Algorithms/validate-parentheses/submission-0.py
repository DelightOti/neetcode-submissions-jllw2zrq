class Solution:
    def isValid(self, s: str) -> bool:
        
        '''
        create an empty stack
        create a dictionary to store key value pairs of the brackets

        think of the string as a char array
        while character < s.length
        if char is an opening
            push chars in s into the stack
        if char is a closing
            if stack is empty:
                return false
            check if it is the closing for the value in the stack
            if it is not:
                return false
        return true if stack is empty
        '''

        stack = []
        my_dict={
            "(":")",
            "{":"}",
            "[":"]"
        }

        for c in s:
            if c in my_dict:
                stack.append(c)
            else:
                if not stack:
                    return False
                # check if c is closing to value in stack using the dictionary
                if my_dict[stack[-1]]!=c:
                    return False
                
                stack.pop()
        return len(stack)==0
