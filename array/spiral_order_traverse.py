class Solution1(object):
    def spiral(self, matrix):
        """
        input: int[][] matrix
        return: Integer[]
        """
        # write your solution here
        if len(matrix) == 0:
            return []
        r_start, r_end = 0, len(matrix) - 1
        c_start, c_end = 0, len(matrix[0]) - 1
        res = []
        while (r_start <= r_end) and (c_start <= c_end):
            res += self.peel(matrix, r_start, c_start, r_end, c_end)
            r_start += 1
            c_start += 1
            r_end -= 1
            c_end -= 1
        return res

    @staticmethod
    def peel(matrix, r_start, c_start, r_end, c_end):
        res = []
        for j in range(c_start, c_end + 1):
            res.append(matrix[r_start][j])
        for i in range(r_start + 1, r_end + 1):
            res.append(matrix[i][c_end])
        for j in range(c_end - 1, c_start - 1, -1):
            res.append(matrix[r_end][j])
        for i in range(r_end - 1, r_start, -1):
            res.append(matrix[i][c_start])
        return res


class Solution2(object):
    def spiral(self, matrix):
        """
        input: int[][] matrix
        return: Integer[]
        """
        # write your solution here
        num_row = len(matrix)
        num_col = len(matrix[0])
        if num_row == 0 and num_col == 0:
            return []
        r_start, r_end = 0, num_row - 1
        c_start, c_end = 0, num_col - 1
        res = []
        while (r_start <= r_end) and (c_start <= c_end):
            res += self.peel(matrix, r_start, c_start, r_end, c_end)
            r_start += 1
            c_start += 1
            r_end -= 1
            c_end -= 1
        return res

    @staticmethod
    def peel(matrix, r_start, c_start, r_end, c_end):
        if r_start == r_end:
            return matrix[r_start][c_start:c_end + 1]
        elif c_start == c_end:
            res = []
            for i in range(r_start, r_end + 1):
                res.append(matrix[i][c_start])
            return res
        res = matrix[r_start][c_start: c_end + 1]
        for i in range(r_start + 1, r_end):
            res.append(matrix[i][c_end])
        for j in range(c_end, c_start - 1, -1):
            res.append(matrix[r_end][j])
        for i in range(r_end - 1, r_start, -1):
            res.append(matrix[i][c_start])
        return res


if __name__ == "__main__":
    a1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    a2 = [[1]]
    solu = Solution2()
    print(solu.spiral(a1))
    print(solu.spiral(a2))
