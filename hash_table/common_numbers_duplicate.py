class Solution(object):
    def frequency(self, arr):
        freq = {}
        for i in arr:
            freq[i] = freq.get(i, 0) + 1
        return freq

    def common_num(self, arr1, arr2):
        res = []
        d1 = self.frequency(arr1)
        d2 = self.frequency(arr2)
        for key in d1.keys():
            if key in d2.keys():
                for i in range(min(d1[key], d2[key])):
                    res.append(key)
        res.sort()
        return res


if __name__ == "__main__":
    a1 = [1, 2, 3, 2]
    a2 = [2, 2, 1]
    s1 = Solution()
    res1 = s1.common_num(a1, a2)
    print(res1)
