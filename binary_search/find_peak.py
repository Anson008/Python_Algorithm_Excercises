class Solution:
    def find_peak(self, arr, left, right, n):
        mid = (left + right) // 2
        if (mid == 0 or arr[mid] >= arr[mid - 1]) and \
                (mid == n - 1 or arr[mid] >= arr[mid + 1]):
            return mid
        elif mid > 0 and arr[mid] < arr[mid - 1]:
            return self.find_peak(arr, left, mid - 1, n)
        else:
            return self.find_peak(arr, mid + 1, right, n)


if __name__ == "__main__":
    arr1 = [3, 2, 1, 5, 4, 1]
    n = len(arr1)
    solu = Solution()
    res = solu.find_peak(arr1, 0, n - 1, n)
    print(res)



