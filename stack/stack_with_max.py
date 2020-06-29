class Stack:
    def __init__(self):
        self._stack = []

    def is_empty(self):
        return len(self._stack) == 0

    def max(self):
        if not self.is_empty():
            return self._stack[-1][1]
        raise Exception("max(): empty stack")

    def push(self, x):
        tmp = x
        if not self.is_empty():
            tmp = max(tmp, self.max())
        self._stack.append((x, tmp))

    def pop(self):
        if self.is_empty():
            raise Exception("pop(): empty stack")
        elem = self._stack.pop()
        return elem[0]

    def peek(self):
        if not self.is_empty():
            return self._stack[-1]
        return []

# time: O(1)
# space: O(n)


if __name__ == "__main__":
    # example stack: 1, 2, 0, 3, -1
    s1 = Stack()
    s1.push(1)
    print(s1.peek())
    s1.push(2)
    s1.push(0)
    s1.push(3)
    s1.push(-1)
    print("After push -1:", s1.peek())
    s1.pop()
    print("After 1 pop:", s1.peek())
    s1.pop()
    print("After 2 pops:", s1.peek())

