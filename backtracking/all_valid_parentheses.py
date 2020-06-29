class Solution:
    def bt_parenthesis(self, answers, sequence, l, r):
        """
        :param answers: list of strings
        :param sequence: list
        :param l: int, number of remaining left parentheses
        :param r: int, number of remaining right parentheses
        :return: None
        """
        if r == 0:
            answers.append(''.join(sequence))
            return
        if l > 0:
            sequence.append('(')
            self.bt_parenthesis(answers, sequence, l - 1, r)
            sequence.pop()
        if l < r:
            sequence.append(')')
            self.bt_parenthesis(answers, sequence, l, r - 1)
            sequence.pop()
        return

    def generate_parenthesis(self, n):
        answers, sequence = [], []
        self.bt_parenthesis(answers, sequence, n, n)
        return answers


if __name__ == "__main__":
    solu = Solution()
    res = solu.generate_parenthesis(2)
    print(res)