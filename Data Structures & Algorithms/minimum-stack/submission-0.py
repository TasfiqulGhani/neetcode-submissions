class MinStack:

    def __init__(self):
        self.min = []
        self.stack = []
        return
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min and self.min[-1] < val:
            self.min.append(self.min[-1])
        else:
            self.min.append(val)


        return
        

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
        return
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
