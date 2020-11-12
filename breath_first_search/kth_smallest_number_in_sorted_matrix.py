import heapq


class Solution:
    @staticmethod
    def kth_smallest(matrix, k):
        """
        input: int[][] matrix, int k
        return: int
        """
        res = []
        visited = set()
        heapq.heappush(res, (matrix[0][0], 0, 0))
        visited.add((0, 0))
        for i in range(1, k):
            curr = heapq.heappop(res)
            if (curr[1] + 1 < len(matrix)) and (curr[1] + 1, curr[2]) not in visited:
                heapq.heappush(res, (matrix[curr[1] + 1][curr[2]], curr[1] + 1, curr[2]))
                visited.add((curr[1] + 1, curr[2]))
            if (curr[2] + 1 < len(matrix[0])) and (curr[1], curr[2] + 1) not in visited:
                heapq.heappush(res, (matrix[curr[1]][curr[2] + 1], curr[1], curr[2] + 1))
                visited.add((curr[1], curr[2] + 1))
        return matrix[res[0][1]][res[0][2]]


if __name__ == "__main__":
    m1 = [[1, 2, 3, 4], [11, 12, 13, 14], [15, 16, 17, 18], [19, 20, 21, 22]]
    k = 4

    solu = Solution()
    print(solu.kth_smallest(m1, k))
