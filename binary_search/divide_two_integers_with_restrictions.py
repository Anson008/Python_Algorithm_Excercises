class Solution(object):
    @staticmethod
    def divide(a, b):
        """
        input: int a, int b
        return: int
        """
        # write your solution here
        max_value = 2147483647
        if b == 0:
            return max_value
        if (a < 0) ^ (b < 0):
            sign = -1
        else:
            sign = 1
        a = abs(a)
        b = abs(b)
        temp = 0
        quotient = 0
        for i in range(31, -1, -1):
            if temp + (b << i) <= a:
                temp += b << i
                quotient += 1 << i
        return sign * quotient
