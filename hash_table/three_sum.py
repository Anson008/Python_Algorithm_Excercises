class Solution:
    @staticmethod
    def three_sum(arr, target):
        if not arr:
            return False
        arr.sort()
        for i in range(len(arr) - 2):
            start = i + 1
            end = len(arr) - 1
            while start < end:
                temp_sum = arr[start] + arr[end] + arr[i]
                if temp_sum < target:
                    start += 1
                elif temp_sum > target:
                    end -= 1
                else:
                    return True
        return False

    @staticmethod
    def three_sum_three_arrays(arr1, arr2, arr3, target):
        arr1_hash = set(arr1)
        for num3 in arr3:
            for num2 in arr2:
                if target - num3 - num2 in arr1_hash:
                    return True
        return False

    @staticmethod
    def three_sum_all_triples(array, target):
        if not array:
            return None
        res = []
        array.sort()
        for i in range(len(array) - 2):
            if i > 0 and array[i] == array[i - 1]:
                continue
            left = i + 1
            right = len(array) - 1
            while left < right:
                temp_sum = array[left] + array[right]
                if array[i] + temp_sum == target:
                    res.append([array[i], array[left], array[right]])
                    left += 1
                    while left < right and array[left] == array[left - 1]:
                        left += 1
                elif temp_sum + array[i] < target:
                    left += 1
                else:
                    right -= 1
        return res

    def three_sum_smaller(self, array, target):
        array.sort()
        count = 0
        for i in range(len(array) - 2):
            start = i + 1
            end = len(array) - 1
            while start < end:
                three_sum = array[i] + array[start] + array[end]
                if three_sum < target:
                    count += end - start
                    start += 1
                else:
                    end -= 1
        return count


if __name__ == "__main__":
    arr1 = [1, 4, 7, 10, 13]
    solu = Solution()
    res1 = solu.three_sum(arr1, target=18)
    print(res1)
