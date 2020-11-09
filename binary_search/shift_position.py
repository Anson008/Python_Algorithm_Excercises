class Solution(object):
    @staticmethod
    def shift_position(array):
        """
        input: int[] array
        return: int
        """
        # write your solution here
        n = len(array)
        if n == 0:
            return -1
        left, right = 0, n - 1
        while left < right - 1:
            mid = (left + right) // 2
            if array[mid] > array[mid + 1]:
                return mid + 1
            if array[mid] < array[mid - 1]:
                return mid
            if array[left] > array[mid]:
                right = mid
            else:
                left = mid
        if array[left] < array[right]:
            if right < n - 1:
                return right + 1
            else:
                return 0
        else:
            return right

