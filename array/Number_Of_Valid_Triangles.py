class Solution(object):
    @staticmethod
    def num_of_triangles(array):
        """
        input: int[] array
        return: int
        """
        # write your solution here
        array.sort()
        n = len(array) - 1
        count = 0
        for i in range(n, 0, -1):
            left = 0
            right = i - 1
            while left < right:
                if array[left] + array[right] > array[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count
