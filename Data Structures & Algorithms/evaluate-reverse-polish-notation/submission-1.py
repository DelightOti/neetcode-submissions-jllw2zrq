class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        '''
        create a stack

        iterate over tokens
            if i is a number:
                pop it into stack
            elif i is +,-,* or /:
                b=stack.pop()
                a=stack.pop()
                number= do a operation b
                and push that back into the stack
        at the end im going to have a number in stack so return that
        '''

        stack=[]

        ops={"+","-","*","/"}
        for i in tokens:
            if i not in ops:
                stack.append(int(i))
            else:
                b=stack.pop()
                a=stack.pop()

                if i == "+":
                    number=a+b
                elif i == "-":
                    number=a-b
                elif i == "*":
                    number=a*b
                else:
                    number=int(a/b)
                stack.append(int(number))
        return stack[-1]