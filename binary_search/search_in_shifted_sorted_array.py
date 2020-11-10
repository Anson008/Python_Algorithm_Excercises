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


class Solution2(object):
    @staticmethod
    def find_pivot(array):
        left, right = 0, len(array) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if array[mid] == array[left]:
                left += 1
            if array[mid] == array[right]:
                right -= 1
            if array[mid] > array[mid + 1]:
                return mid
            if array[mid] < array[mid - 1]:
                return mid - 1
            if array[mid] > array[left]:
                left = mid
            if array[mid] < array[left]:
                right = mid
        if array[left] > array[right]:
            return left
        else:
            return right

    @staticmethod
    def find_first_occurrence(array, target, left, right):
        while left < right - 1:
            mid = (left + right) // 2
            if array[mid] < target:
                left = mid + 1
            elif array[mid] > target:
                right = mid - 1
            else:
                right = mid
        if array[left] == target:
            return left
        if array[right] == target:
            return right
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
        if target < array[start]:
            return self.find_first_occurrence(array, target, pivot + 1, n - 1)
        else:
            return self.find_first_occurrence(array, target, 0, pivot)


if __name__ == "__main__":
    solu = Solution2()
    a1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        # 0, 1, 2 ,3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20,21
    print(len(a1))
    a2 = [1, 1, 1, 1, 2]
    target = 2
    print(solu.find_pivot(a2))
    #print(solu.search(a1, target))


