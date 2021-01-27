class Solution(object):
    def search(self, matrix):
        """
        input: int[][] matrix
        return: int
        """
        # write your solution here
        if len(matrix) <= 1:
            return -1
        idx = 0
        common = matrix[0]
        # res = -1
        for i in range(1, len(matrix)):
            new = []
            for x in common:
                idx = self.bi_search(matrix[i], x)
                if idx > -1:
                    new.append(matrix[i][idx])
            common = new
        if len(common) >= 1:
            return common[0]
        else:
            return -1

    @staticmethod
    def bi_search(arr, target):
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] < target:
                l = mid + 1
            elif arr[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1
