class TwoSumPair:
    def __init__(self, arr, index1, index2):
        self.index1 = index1
        self.index2 = index2
        self.number1 = arr[index1]
        self.number2 = arr[index2]
        self.sum = self.number1 + self.number2


class Solution:
    @staticmethod
    def two_sum_on_pair(arr, target):
        pair_list = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                pair_list.append(TwoSumPair(arr, i, j))
        hashset = dict()
        for x in pair_list:
            if target - x.sum in hashset:
                y = hashset[target - x.sum]
                if (x.index1 != y.index1 and x.index1 != y.index2
                        and x.index2 != y.index1 and x.index2 != y.index2):
                    return x.number1, x.number2, y.number1, y.number2
            else:
                hashset[x.sum] = x
        return None


if __name__ == "__main__":
    solu = Solution()
    arr1 = [1, 4, 7, 10, 13]
    res1 = solu.two_sum_on_pair(arr1, target=22)
    print(res1)
