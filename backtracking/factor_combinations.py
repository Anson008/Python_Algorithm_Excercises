import math


class Solution1(object):
    def bt_factor(self, answers, comb, n):
        if len(comb) > 0:
            answers.append(comb + [n])
        for f in range(2 if not comb else comb[-1], int(math.sqrt(n)) + 1):
            if n % f == 0:
                comb.append(f)
                self.bt_factor(answers, comb, n // f)
                comb.pop()

    def get_factors(self, n):
        answers, comb = [], []
        self.bt_factor(answers, comb, n)
        return answers


class Solution2(object):
    def bt_factor(self, answers, comb, s, n):
        if s * s <= n:
            if n % s == 0:
                answers.append(comb + [s, n // s])
                self.bt_factor(answers, comb + [s], s, n // s)
            s += 1

    def get_factors(self, n):
        answers = []
        self.bt_factor(answers, [], 2, n)
        return answers


if __name__ == "__main__":
    solu1 = Solution1()

    res1 = solu1.get_factors(0)
    print("res1:", res1)

    res2 = solu1.get_factors(1)
    print("res2:", res2)

    res3 = solu1.get_factors(2)
    print("res3:", res3)

    res4 = solu1.get_factors(12)
    print("res4:", res4)

    res5 = solu1.get_factors(4)
    print("res4:", res5)