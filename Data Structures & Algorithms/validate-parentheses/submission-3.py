class Solution:
    def isValid(self, s: str) -> bool:

        '''
        Create a hashmap and store each opening bracket with the correct closing bracket

        create a stack []
        iterate over my string s
            if it is an opening bracket:
                push it into my stack
            else it is a closing bracket:
                pop the top element of my stack and check thru my hashmap if
                the closing is correct for that opening
                if its not return False
        return True
        '''

        my_dict={
            "(":")",
            "{":"}",
            "[":"]"
        }

        stack=[]

        for i in s:
            if i in my_dict:
                stack.append(i)
            else:
                if not stack:
                    return False
                c = stack.pop()
                if my_dict[c] != i:
                    return False
        return True if len(stack)==0 else False