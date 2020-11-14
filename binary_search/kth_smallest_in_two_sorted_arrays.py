class Solution1(object):
    def kth(self, a, b, k):
        """
        input: int[] a, int[] b, int k
        return: int
        """
        # write your solution here
        len_a = len(a)
        len_b = len(b)
        if len_a == 0 and len_b != 0:
            return b[k - 1]
        if len_a != 0 and len_b == 0:
            return a[k - 1]
        i, j = 0, 0
        res = 0
        count = 0
        while i < len_a and j < len_b:
            if a[i] <= b[j]:
                res = a[i]
                count += 1
                if count == k:
                    return res
                i += 1
            else:
                res = b[j]
                count += 1
                if count == k:
                    return res
                j += 1
        while i < len_a:
            if count == k:
                return res
            res = a[i]
            count += 1
        while j < len_b:
            if count == k:
                return res
            res = b[j]
            count += 1

