class Solution:
    @staticmethod
    def local_maximum(array):
        left, right = 0, len(array) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if array[mid] > array[mid - 1] and array[mid] > array[mid + 1]:
                return mid
            elif array[mid] < array[mid - 1]:
                right = mid
            else:
                left = mid
        if array[left] > array[right]:
            return left
        else:
            return right

    @staticmethod
    def local_minimum(array):
        left, right = 0, len(array) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if array[mid] < array[mid - 1] and array[mid] < array[mid + 1]:
                return mid
            elif array[mid] > array[mid - 1]:
                right = mid
            else:
                left = mid
        if array[left] < array[right]:
            return left
        else:
            return right


if __name__ == "__main__":
    arr1 = [3, 2, 1, 5, 4, 1]
    solu = Solution()
    print(solu.local_maximum(arr1))
    print(solu.local_minimum(arr1))



