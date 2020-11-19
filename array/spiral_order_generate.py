class Solution1(object):
    def spiralGenerate(self, n):
        """
        input: int n
        return: int[][]
        """
        # write your solution here
        if n == 0:
            return []
        res = [[0 for i in range(n)] for j in range(n)]
        return self.roll(res, 0, n - 1, 0, n - 1)

    def roll(self, res, top, bottom, left, right):
        if (top == bottom) and (left == right):
            res[top][left] = res[top][left - 1] + 1
            return res
        if (top > bottom) and (left > right):
            return res
        for j in range(left, right + 1):
            if j == 0 and top == 0:
                res[top][j] = 1
            else:
                res[top][j] = res[top][j - 1] + 1
        for i in range(top + 1, bottom + 1):
            res[i][right] = res[i - 1][right] + 1
        for j in range(right - 1, left - 1, - 1):
            res[bottom][j] = res[bottom][j + 1] + 1
        for i in range(bottom - 1, top, - 1):
            res[i][left] = res[i + 1][left] + 1
        self.roll(res, top + 1, bottom - 1, left + 1, right - 1)
        return res


class Solution2(object):
    def spiralGenerate(self, m, n):
        """
        input: int m, int n
        return: int[][]
        """
        # write your solution here
        if m == 0 and n == 0:
            return []
        res = [[0 for j in range(n)] for i in range(m)]
        return self.roll(res, 0, m - 1, 0, n - 1)

    def roll(self, res, top, bottom, left, right):
        if top == bottom:
            for j in range(left, right + 1):
                res[top][j] = res[top][j - 1] + 1
            return res
        if left == right:
            for i in range(top, bottom + 1):
                if i == top:
                    res[i][left] = res[i][left - 1] + 1
                else:
                    res[i][left] = res[i - 1][left] + 1
            return res
        if top > bottom or left > right:
            return res
        for j in range(left, right + 1):
            if j == 0 and top == 0:
                res[top][j] = 1
            else:
                res[top][j] = res[top][j - 1] + 1
        for i in range(top + 1, bottom + 1):
            res[i][right] = res[i - 1][right] + 1
        for j in range(right - 1, left - 1, -1):
            res[bottom][j] = res[bottom][j + 1] + 1
        for i in range(bottom - 1, top, -1):
            res[i][left] = res[i + 1][left] + 1
        self.roll(res, top + 1, bottom - 1, left + 1, right - 1)
        return res


if __name__ == "__main__":
    n = 2
    solu = Solution1()
    print(solu.spiralGenerate(n))