import heapq


class Solution:
    def num_apples(self, array):
        cap_available = 5000 - array[0]
        apples = array[1:]
        heapq.heapify(apples)
        count = 0
        while cap_available > 0:
            cap_available -= heapq.heappop(apples)
            if cap_available >= 0:
                count += 1
        return count