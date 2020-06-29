import random


class Generator(object):
    def __init__(self):
        self.counter = 0
        self.max_value = float('-inf')
        self.index = -1
        self.sample = 0

    def read(self, val):
        self.index += 1
        if val > self.max_value:
            self.max_value = val
            self.counter += 1
            self.sample = self.index
        elif val == self.max_value:
            self.counter += 1
            r = random.randint(0, self.counter - 1)
            if r == 0:
                self.sample = self.index

    def get_sample(self):
        return self.sample

