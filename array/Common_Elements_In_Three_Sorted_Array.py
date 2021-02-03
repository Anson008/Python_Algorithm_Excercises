class Solution(object):
    def common(self, a, b, c):
        """
        input: int[] a, int[] b, int[] c
        return: Integer[]
        """
        # write your solution here
        d = self.compare_two(a, b)
        return self.compare_two(d, c)

    @staticmethod
    def compare_two(a, b):
        i, j = 0, 0
        res = []
        while i < len(a) and j < len(b):
            if a[i] > b[j]:
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                res.append(a[i])
                i += 1
                j += 1
        return res
