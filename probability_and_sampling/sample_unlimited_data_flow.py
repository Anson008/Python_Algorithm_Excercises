import random


class Generator(object):
    def __init__(self):
        self.counter = 0
        self.sample = 0

    def read(self, value):
        self.coutner += 1
        r = random.randint(0, self.counter - 1)
        if r == 0:
            self.sample = value

    def get_sample(self):
        return self.sample

