class Solution(object):
    def common_num(self, arr1, arr2):
        s1 = set(arr1)
        s2 = set(arr2)
        res = list(s1.intersection(s2))
        res.sort()
        return res


if __name__ == "__main__":
    a1 = [1, 2, 3, 2]
    a2 = [3, 1]
    s1 = Solution()
    res1 = s1.common_num(a1, a2)
    print(res1)
