class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x):
        self.stack.append(x)
        if len(self.min) == 0 or x <= self.get_min():
            self.min.append(x)

    def pop(self):
        if self.stack[-1] == self.get_min():
            self.min.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min[-1]