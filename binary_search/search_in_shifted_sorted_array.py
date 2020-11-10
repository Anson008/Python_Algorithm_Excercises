class Solution(object):
    @staticmethod
    def find_pivot(array):
        left, right = 0, len(array) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if array[mid] > array[mid + 1]:
                return mid
            if array[mid] < array[mid - 1]:
                return mid - 1
            if array[mid] > array[left]:
                left = mid
            else:
                right = mid
        if array[left] > array[right]:
            return left
        else:
            return right

    @staticmethod
    def binary_search(array, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if array[mid] < target:
                left = mid + 1
            elif array[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

    def search(self, array, target):
        """
        input: int[] array, int target
        return: int
        """
        # write your solution here
        n = len(array)
        if n == 0:
            return -1
        pivot = self.find_pivot(array)
        start = 0
        if target > array[start]:
            return self.binary_search(array, 0, pivot, target)
        elif target < array[start]:
            return self.binary_search(array, pivot + 1, n - 1, target)
        else:
            return start



