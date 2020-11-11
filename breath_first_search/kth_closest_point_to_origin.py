import heapq


class Solution(object):
    @staticmethod
    def closest(a, b, c, k):
        """
        input: int[] a, int[] b, int[] c, int k
        return: Integer[]
        """
        # write your solution here
        visited = set()
        res = []
        heapq.heappush(res, (a[0]**2 + b[0]**2 + c[0]**2, 0, 0, 0))
        visited.add((0, 0, 0))
        for i in range(1, k):
            curr = heapq.heappop(res)
            if (curr[1] + 1 < len(a)) and (curr[1] + 1, curr[2], curr[3]) not in visited:
                heapq.heappush(res, (a[curr[1] + 1]**2 + b[curr[2]]**2 + c[curr[3]]**2, curr[1] + 1, curr[2], curr[3]))
                visited.add((curr[1] + 1, curr[2], curr[3]))
            if (curr[2] + 1 < len(b)) and (curr[1], curr[2] + 1, curr[3]) not in visited:
                heapq.heappush(res, (a[curr[1]]**2 + b[curr[2] + 1]**2 + c[curr[3]]**2, curr[1], curr[2] + 1, curr[3]))
                visited.add((curr[1], curr[2] + 1, curr[3]))
            if (curr[3] + 1 < len(c)) and (curr[1], curr[2], curr[3] + 1) not in visited:
                heapq.heappush(res, (a[curr[1]]**2 + b[curr[2]]**2 + c[curr[3] + 1]**2, curr[1], curr[2], curr[3] + 1))
                visited.add((curr[1], curr[2], curr[3] + 1))
            if len(res) == 0:
                heapq.heappush(res, curr)
        return [a[res[0][1]], b[res[0][2]], c[res[0][3]]]


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [2, 4]
    c = [1, 2]
    k = 10

    solu = Solution()
    print(solu.closest(a, b, c, k))
