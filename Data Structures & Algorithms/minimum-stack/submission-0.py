class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.prefix) == 0: 
            self.prefix.append(val)
        else:
            self.prefix.append(min(val, self.prefix[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.prefix.pop()

    def top(self) -> int:
        top = self.stack[-1]
        return top

    def getMin(self) -> int:
        return self.prefix[-1]
        
