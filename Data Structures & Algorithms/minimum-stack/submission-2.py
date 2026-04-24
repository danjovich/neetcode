class MinStack:
    elements: list[int]
    min_values: list[int]

    def __init__(self):
        self.elements = list()
        self.min_values = list()

    def push(self, val: int) -> None:
        if len(self.min_values) == 0:
            self.min_values.append(val)
        elif val < self.min_values[-1]:
            self.min_values.append(val)
        else:
            self.min_values.append(self.min_values[-1])

        self.elements.append(val)

    def pop(self) -> None:
        self.elements.pop()
        self.min_values.pop()

    def top(self) -> int:
        return self.elements[-1]

    def getMin(self) -> int:
        return self.min_values[-1]


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(1)
    minStack.push(2)
    minStack.push(0)
    assert minStack.getMin() == 0
    minStack.pop()
    assert minStack.top() == 2
    assert minStack.getMin() == 1
