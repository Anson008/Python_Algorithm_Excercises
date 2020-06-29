import random


def random5():
    return random.randint(1, 5)


def random2():
    return random.randint(1, 2)


class Random7(object):
    def __init__(self):
        self.sample = 0

    def random25(self):
        return random5() + 5 * random5()

    def random7(self):
        num = self.random25()
        while num > 20:
            num = self.random25()
        self.sample = num % 7

    def get_sample(self):
        self.random7()
        return self.sample


class RandomXWithRandomM(object):
    def __init__(self):
        self.sample = 0

    def rand_x(self, x, m):
        num = random.randint(0, m)
        curr_num_candidates = m
        while curr_num_candidates < x or num >= x:
            if num >= x:
                num = random.randint(0, m)
                curr_num_candidates = m
            else:
                num = num * m + random.randint(0, m)
                curr_num_candidates = m * curr_num_candidates
        return num

    def get_sample(self, x, m):
        self.sample = self.rand_x(x, m)
        return self.sample


if __name__ == "__main__":
    random7 = Random7()
    print(random7.get_sample())



