import random


class Solution:
    def quick_sort(self, array):
        if len(array) == 0:
            return []
        self._quick_sort(array, 0, len(array) - 1)
        return array

    def _quick_sort(self, array, left, right):
        if left >= right:
            return
        pivot = array[random.randint(left, right)]
        index = self._partition(array, left, right, pivot)
        self._quick_sort(array, left, index - 1)
        self._quick_sort(array, index, right)

    @staticmethod
    def _partition(array, left, right, pivot):
        while left <= right:
            while left <= right and array[left] < pivot:
                left += 1
            while left <= right and array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        return left


class Solution2:
    def quick_sort(self, arr):
        if len(arr) == 0:
            return []
        self._quick_sort(arr, 0, len(arr) - 1)
        return arr

    def _quick_sort(self, arr, start, end):
        if start >= end:
            return
        pivot_index = random.randrange(start, end + 1)
        new_pivot_index = self._partition(arr, start, end, pivot_index)
        self._quick_sort(arr, start, new_pivot_index - 1)
        self._quick_sort(arr, new_pivot_index + 1, end)

    @staticmethod
    def _partition(arr, start, end, pivot_index):
        arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
        store_index = start
        pivot = arr[end]
        for i in range(start, end):
            if arr[i] < pivot:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        arr[store_index], arr[end] = arr[end], arr[store_index]
        return store_index

# time: average O(n*log(n)), worst O(n^2)
# space: average O(log(n)), worst O(n)


if __name__ == "__main__":
    a1 = [3, 3, 1, 7, 2, 9, 17, 45, 24]
    a2 = [28, 2, -1, 4]
    a3 = []

    test = [a1, a2, a3]

    solu = Solution()
    solu2 = Solution2()
    for l in test:
        print("Solution 1:", solu.quick_sort(l))
        print("Solution 2:", solu2.quick_sort(l))








