class Solution(object):
    def sqrt(self, x):
        left = 0
        right = x
        if right ** 2 == x:
            return right
        while left < right - 1:
            mid = (left + right) // 2
            if mid ** 2 > x:
                right = mid
            elif mid ** 2 < x:
                left = mid
            else:
                return mid
        return left


if __name__ == "__main__":
    solu = Solution()
    res1 = solu.sqrt(18)
    print("res1:", res1)
    res2 = solu.sqrt(4)
    print("res2:", res2)
    res3 = solu.sqrt(1)
    print("res3:", res3)
    res4 = solu.sqrt(17)
    print("res4:", res4)