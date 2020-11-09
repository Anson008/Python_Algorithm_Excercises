class Solution:
    def missing_num(self, array):
        """
        :param array: List[int]
        :return: int
        """
        n = len(array)
        if n == 0:
            return 1
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if array[mid] - mid == 1:
                left = mid + 1
            if array[mid] - mid == 2:
                right = mid - 1
        return left + 1