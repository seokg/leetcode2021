class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, val: int) -> None:
        self.stack += [val]

    def pop(self) -> None:
        if len(self.stack)==0:
            return None
        last = self.stack[-1]
        self.stack[:] = self.stack[0:-1] 

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        if len(self.stack)==0:
            return None
        return min(self.stack)
        
        