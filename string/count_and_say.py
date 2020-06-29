import itertools


class Solution(object):
    @staticmethod
    def count_and_say(n):
        res = '1'
        for i in range(n-1):
            subsequent_digits = ''
            for key, group in itertools.groupby(res):
                count = len(list(group))
                subsequent_digits += '{:d}{:s}'.format(count, key)
            res = subsequent_digits
        return res


if __name__ == "__main__":
    countSay = Solution()
    res1 = countSay.count_and_say(5)
    print(res1)