class Solution(object):
    def interleave(self, array):
        """
        input: int[] array
        return: int[]
        """
        # write your solution here
        pos_start = self.partition(array)
        i, j = 0, pos_start
        while i < j < len(array):
            array[i], array[j] = array[j], array[i]
            i += 2
            j += 1
        return array

    @staticmethod
    def partition(array):
        left, right = 0, len(array) - 1
        while left <= right:
            while left <= right and array[left] < 0:
                left += 1
            while left <= right and array[right] > 0:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        return left

    @staticmethod
    def partition2(array):
        i = -1
        for j in range(len(array)):
            if array[j] < 0:
                i += 1
                array[i], array[j] = array[j], array[i]
        return i + 1
