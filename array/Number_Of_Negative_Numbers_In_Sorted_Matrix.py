class Solution(object):
    @staticmethod
    def neg_number(matrix):
        """
        input: int[][] matrix
        return: int
        """
        # write your solution here
        nrows = len(matrix)
        ncols = len(matrix[0])
        i = 0
        j = ncols - 1
        count = 0
        while i < nrows and j >= 0:
            if matrix[i][j] < 0:
                count += j + 1
                i += 1
            else:
                j -= 1
        return count
