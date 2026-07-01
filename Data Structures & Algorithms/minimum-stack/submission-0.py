class MinStack:

    def __init__(self):
    #initialize 2 stacks/arrays
        self.stack = []
        self.minStack = []  

    def push(self, val: int) -> None:
    #pushing the input value into our first stack
        self.stack.append(val)
    #push the minimum value in our minstack by finding the minimum of input and minstack
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    
    def getMin(self) -> int:
        return self.minStack[-1]
        
