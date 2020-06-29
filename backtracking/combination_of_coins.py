class Solution:
    def bt_coin(self, answers, comb, coins, level, money_left):
        if level == len(coins):
            if money_left == 0:
                answers.append(comb[:])
            return
        for t in range(money_left // coins[level] + 1):
            comb.append(t)
            self.bt_coin(answers, comb, coins, level + 1, money_left - t * coins[level])
            comb.pop()

    def generate_coin_combinations(self, coins, money_left):
        answers, comb = [], []
        self.bt_coin(answers, comb, coins, 0, money_left)
        return answers

    @staticmethod
    def print_answers(combs):
        for comb in combs:
            print(comb)


if __name__ == "__main__":
    coins1 = [25, 10, 5, 1]
    coins2 = [2, 1]
    solu = Solution()
    res1 = solu.generate_coin_combinations(coins1, 99)
    res2 = solu.generate_coin_combinations(coins2, 4)
    solu.print_answers(res2)

