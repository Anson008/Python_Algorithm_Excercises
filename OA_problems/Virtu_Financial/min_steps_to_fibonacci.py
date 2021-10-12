class Solution:
    def min_step(self, n):
        a = 0
        b = 1
        c = 1
        left = right = 0
        while True:
            a = b
            b = c
            c = a + b
            if c < n:
                left = n - c
            else:
                right = c - n
                break
        return min(left, right)