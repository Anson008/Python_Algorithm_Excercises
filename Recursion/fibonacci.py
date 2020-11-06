class Solution:
    def fibonacci_recursion(self, n):
        if n <= 1:
            return 0, n
        else:
            a, b = self.fibonacci_recursion(n - 1)
            return b, a + b

    @staticmethod
    def fibonacci_iteration(n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a


if __name__ == "__main__":
    solu = Solution()
    n = 6
    print(solu.fibonacci_recursion(n))
    print(solu.fibonacci_iteration(n))