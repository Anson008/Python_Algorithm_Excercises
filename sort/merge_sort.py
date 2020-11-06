class Solution(object):
    def merge_sort(self, array):
        """
        input: int[] array
        return: int[]
        """
        # write your solution here
        if len(array) == 0 or len(array) == 1:
            return array
        mid = len(array) // 2
        left = self.merge_sort(array[:mid])
        right = self.merge_sort(array[mid:])
        return self._merge(left, right)

    @staticmethod
    def _merge(arr1, arr2):
        i, j = 0, 0
        res = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        while i < len(arr1):
            res.append(arr1[i])
            i += 1
        while j < len(arr2):
            res.append(arr2[j])
            j += 1
        return res


# time: O(n*log(n))
# space: O(n)


if __name__ == "__main__":
    a1 = [3, 27, 38, 43]
    a2 = [3, 10, 82]
    a3 = [4, 1, 12, 45, 98, 12, 23]

    test = [a1, a2, a3]
    solu = Solution()

    for arr in test:
        print("Original: ", arr)
        print("Sorted: ", solu.merge_sort(arr))
