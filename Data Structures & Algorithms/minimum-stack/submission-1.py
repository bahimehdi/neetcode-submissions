class MinStack:

    def __init__(self):
        self.minStack = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.minStack.append(val)
        if not self.minimum or val <= self.minimum[-1]:
            self.minimum.append(val)

    def pop(self) -> None:
        minima = self.minStack.pop()
        if minima == self.minimum[-1]:
            self.minimum.pop()

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
