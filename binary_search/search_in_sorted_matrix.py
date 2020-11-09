class Solution:
    @staticmethod
    def search_2d(matrix, target):
        """
        :param matrix: List[List[int]]
        :param target: int
        :return: List[int]
        """
        M = len(matrix)
        N = len(matrix[0])
        i, j = 0, M - 1
        while i < N and j >= 0:
            if target < matrix[i][j]:
                j -= 1
            elif target > matrix[i][j]:
                i += 1
            else:
                return [i, j]
        return [-1, -1]