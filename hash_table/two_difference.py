class Solution:
    @staticmethod
    def two_difference_sorted(arr, target):
        i = 0
        j = 1
        target = abs(target)
        while i < len(arr) and j < len(arr):
            if arr[j] - arr[i] < target:
                j += 1
            elif arr[j] - arr[i] > target:
                i += 1
            else:
                return True
        return False

    @staticmethod
    def two_difference_unsorted(arr, target):
        hashset = set()
        for x in arr:
            if x - target in hashset or x + target in hashset:
                return True
            else:
                hashset.add(x)
        return False


if __name__ == "__main__":
    arr1 = [1, 4, 6, 10, 13]
    arr2 = [4, 1, 18, 5, 2, 9]
    solu = Solution()
    res1 = solu.two_difference_sorted(arr1, target=2)
    res2 = solu.two_difference_unsorted(arr2, target=6)
    print(res1)
    print(res2)