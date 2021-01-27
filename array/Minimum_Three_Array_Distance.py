class Solution(object):
    @staticmethod
    def min_distance(a, b, c):
        """
        input: int[] a, int[] b, int[] c
        return: int
        """
        # write your solution here
        al, bl, cl = len(a), len(b), len(c)
        i, j, k = 0, 0, 0
        idx_i, idx_j, idx_k = 0, 0, 0
        diff = float("inf")
        while i < al and j < bl and k < cl:
            minimum = min(a[i], min(b[j], c[k]))
            maximum = max(a[i], max(b[j], c[k]))
            if maximum - minimum < diff:
                diff = maximum - minimum
                idx_i = i
                idx_j = j
                idx_k = k
            if diff == 0:
                break
            if a[i] == minimum:
                i += 1
            elif b[j] == minimum:
                j += 1
            else:
                k += 1
        return abs(a[idx_i] - b[idx_j]) + abs(b[idx_j] - c[idx_k]) + abs(a[idx_i] - c[idx_k])
