class Solution1(object):
    @staticmethod
    def rainbow_sort(array):
        curr = 0
        left = 0
        right = len(array) - 1
        while curr <= right:
            if array[curr] == 0:
                curr += 1
            elif array[curr] == 1:
                array[curr], array[right] = array[right], array[curr]
                right -= 1
            else:
                array[curr], array[left] = array[left], array[curr]
                curr += 1
                left += 1
        return array


class Solution2(object):
    def rainbow_sort(self, array, k):
        """
        input: int[] array, int k
        return: int[]
        """
        # write your solution here
        n = len(array)
        if n <= 1:
            return array
        self.partition(array, 0, n - 1, 0, k - 1)
        return array

    def partition(self, array, start, end, color_from, color_to):
        if start == end:
            return
        if color_from == color_to:
            return
        color_mid = (color_from + color_to) // 2
        left, right = start, end
        while left <= right:
            while left <= right and array[left] <= color_mid:
                left += 1
            while left <= right and array[right] > color_mid:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        self.partition(array, start, right, color_from, color_mid)
        self.partition(array, left, end, color_mid + 1, color_to)


if __name__ == "__main__":
    a1 = [1, 0, 1, 0, 0, -1, 1, -1]
    a2 = [2, 1, 0, 3, 2, 0, 1, 3]
    solu = Solution2()
    print(solu.rainbow_sort(a2, 4))