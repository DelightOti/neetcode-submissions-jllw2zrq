class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]

    def push(self, val: int) -> None:
        '''
        append value to stack
        if minstack is empty
            currentmin=val
        else minstack is not empty:
            previousmin= top of stack
            if previousmin<currentmin:
                currentmin=previousmin
            else:
                currentmin=val
        push currentmin to minstack
            
        '''
        self.stack.append(val)
        if not self.minstack:
            current_min=val
        else:
            previous_min = self.minstack[-1]
            if previous_min<val:
                current_min=previous_min
            else:
                current_min=val
        
        self.minstack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.minstack[-1]
        
