class Solution(object):
    @staticmethod
    def rotate(matrix):
        """
        input: int[][] matrix
        return: No need to return
        """
        # write your solution here
        n = len(matrix)
        if n == 0:
            return []
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
        return matrix

