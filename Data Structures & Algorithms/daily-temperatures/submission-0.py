class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        create a stack
        create a res list the size of temperature

        iterate over the stack
            create another loop while the stack has smth and the currentvalue > value at top of stack:
                x=stack.pop()
                prev_index=x[1]
                prev_value=x[0]
                add it to the prev_index

            add the current value to stack
        
        return res
        '''

        stack=[]
        res=[0]*len(temperatures)

        for i, value in enumerate(temperatures):
            while stack and value>stack[-1][0]:
                x=stack.pop()
                prev_index=x[1]
                prev_value=x[0]
                res[prev_index]=i-prev_index

            stack.append((value,i))
        return res