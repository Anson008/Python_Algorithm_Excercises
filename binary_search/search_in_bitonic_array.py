class Solution(object):
    @staticmethod
    def find_maximum(array):
        left, right = 0, len(array) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if (array[mid] > array[mid - 1]) and (array[mid] > array[mid + 1]):
                return mid
            if array[mid - 1] < array[mid] < array[mid + 1]:
                left = mid
            if array[mid - 1] > array[mid] > array[mid + 1]:
                right = mid
        if array[left] < array[right]:
            return right
        else:
            return left

    @staticmethod
    def binary_search(array, target, left, right, direction):
        if direction == 'ASC':
            while left <= right:
                mid = (left + right) // 2
                if array[mid] < target:
                    left = mid + 1
                elif array[mid] > target:
                    right = mid - 1
                else:
                    return mid
            return -1
        if direction == 'DESC':
            while left <= right:
                mid = (left + right) // 2
                if array[mid] < target:
                    right = mid - 1
                elif array[mid] > target:
                    left = mid + 1
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
        max_idx = self.find_maximum(array)
        start, end = 0, n - 1
        if target == array[max_idx]:
            return max_idx
        else:
            res1 = self.binary_search(array, target, start, max_idx - 1, 'ASC')
            res2 = self.binary_search(array, target, max_idx + 1, end, 'DESC')
            if res1 >= 0 > res2:
                return res1
            if res1 < 0 <= res2:
                return res2
            if res1 < 0 and res2 < 0:
                return -1

if __name__ == "__main__":
    a1 = [1, 3, 5, 8, 6, 2]
    a2 = [-2, 0, 6, 7, 8, 10]

    target = -2
    solu = Solution()
    print(solu.find_maximum(a2))
    print(solu.search(a2, target))
