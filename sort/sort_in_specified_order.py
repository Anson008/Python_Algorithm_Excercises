import heapq


class Solution(object):
    def sort_special(self, a1, a2):
        """
        input: int[] a1, int[] a2
        return: int[]
        """
        # write your solution here
        heap = []
        res = []
        hist = self.histogram(a1)
        for n in a2:
            if n in hist:
                res += [n] * hist[n]
        for key, value in hist.items():
            if key not in a2:
                heapq.heappush(heap, (key, value))
        while len(heap) > 0:
            num, count = heapq.heappop(heap)
            res += [num] * count
        return res

    @staticmethod
    def histogram(a1):
        hist = {}
        for x in a1:
            if x in hist:
                hist[x] += 1
            else:
                hist[x] = 1
        return hist

