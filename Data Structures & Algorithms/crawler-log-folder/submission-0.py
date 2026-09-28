class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        # keeping a log each time a user performs a change folder operation

        stack = []

        for log in logs:
            
            if log == "../":
                if stack:
                    stack.pop()
            elif log != "./":
                stack.append(log)
        return len(stack)
        
                
        

        
    
        