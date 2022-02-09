class MyQueue:

    def __init__(self):
        self.S = []

    def push(self, x: int) -> None:
        self.S.append(x)

    def pop(self) -> int:
        return self.S.pop(0)

    def peek(self) -> int:
        return self.S[0]

    def empty(self) -> bool:
        if self.S:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
