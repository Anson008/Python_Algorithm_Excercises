class Solution:
    @staticmethod
    def two_sum_sorted(arr, target):
        i, j = 0, len(arr) - 1
        while i < j:
            if arr[i] + arr[j] < target:
                i += 1
            elif arr[i] + arr[j] > target:
                j -= 1
            else:
                return True
        return False

    @staticmethod
    def two_sum(arr, target):
        passed = set()
        for x in arr:
            if target - x in passed:
                return True
            else:
                passed.add(x)
        return False

    @staticmethod
    def two_sum_duplicate1(arr, target):
        passed = {}
        count = 0
        for key in arr:
            if target - key in passed:
                count += passed[target - key]
            passed[key] = passed.get(key, 0) + 1
        return count

    @staticmethod
    def two_sum_duplicate2(arr, target):
        passed = {}
        ans = []
        for i in range(len(arr)):
            if target - arr[i] in passed:
                for index in passed[target - arr[i]]:
                    ans.append([i, index])
            if arr[i] in passed:
                passed[arr[i]].append(i)
            else:
                passed[arr[i]] = [i]
        return ans

    @staticmethod
    def two_sum_closest(arr, target):
        arr.sort()
        left = 0
        right = len(arr) - 1
        res = []
        closest = float('inf')
        while left < right:
            two_sum = arr[left] + arr[right]
            if abs(two_sum - target) < closest:
                closest = abs(two_sum - target)
                res = [arr[left], arr[right]]
            if two_sum > target:
                right -= 1
            else:
                left += 1
        return res

    @staticmethod
    def two_sum_smaller(arr, target):
        arr.sort()
        left = 0
        right = len(arr) - 1
        count = 0
        while left < right:
            if arr[left] + arr[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1
        return count

    @staticmethod
    def two_sum_two_array(arr1, arr2, target):
        if not arr1 or not arr2:
            return False
        arr1_hash = set(arr1)
        for x in arr2:
            if target - x in arr1_hash:
                return True
        return False

    @staticmethod
    def two_sum_all_pairs(array, target):
        """
        input: int[] array, int target
        return: int[][]
        """
        array.sort()
        l, r = 0, len(array) - 1
        res = []
        while l < r:
            if array[l] + array[r] > target:
                r -= 1
            elif array[l] + array[r] < target:
                l += 1
            else:
                if array[l] == array[l + 1]:
                    while l < len(array) - 1 and array[l] == array[l + 1]:
                        l += 1
                if array[r] == array[r - 1]:
                    while r > 0 and array[r] == array[r - 1]:
                        r -= 1
                res.append([array[l], array[r]])
                l += 1
                r -= 1
        return res


if __name__ == "__main__":
    nums1 = [1, 2, 3]
    nums2 = [10, 1, 13]
    nums3 = [10, 2, 2, 13, 2]
    solu = Solution()
    res1 = solu.two_sum_sorted(nums1, 5)
    res2 = solu.two_sum(nums2, 11)
    res3 = solu.two_sum_duplicate1(nums3, 4)
    res4 = solu.two_sum_duplicate2(nums3, 4)
    #solu.two_sum_duplicate2(nums3, 4)
    print(res1)
    print(res2)
    print(res3)
    print(res4)