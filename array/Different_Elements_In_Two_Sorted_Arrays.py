class Solution(object):
    def diff(self, a, b):
        """
        input: int[] a, int[] b
        return: int[][]
        """
        # write your solution here
        i, j = 0, 0
        res_a = []
        res_b = []
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                res_a.append(a[i])
                i += 1
            elif a[i] > b[j]:
                res_b.append(b[j])
                j += 1
            else:
                i += 1
                j += 1
        while i < len(a):
            res_a.append(a[i])
            i += 1
        while j < len(b):
            res_b.append(b[j])
            j += 1
        return [res_a, res_b]
