class Solution(object):
    @staticmethod
    def set_zero(matrix):
        """
        input: int[][] matrix
        return: No need to return
        """
        # write your solution here
        if len(matrix) == 0:
            return matrix
        first_row = False
        first_col = False
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        for i in range(0, num_rows):
            if matrix[i][0] == 0:
                first_col = True
                break
        for j in range(0, num_cols):
            if matrix[0][j] == 0:
                first_row = True
                break
        for i in range(1, num_rows):
            for j in range(1, num_cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, num_rows):
            for j in range(1, num_cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row:
            for j in range(num_cols):
                matrix[0][j] = 0
        if first_col:
            for i in range(num_rows):
                matrix[i][0] = 0
