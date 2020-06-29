import heapq


class Solution(object):
    @staticmethod
    def kth_largest_element(arr, k):
        if not arr or k > len(arr):
            return
        k_min_ele = [x for x in arr[0:k]]
        heapq.heapify(k_min_ele)
        for i in range(k, len(arr)):
            if arr[i] > k_min_ele[0]:
                heapq.heappop(k_min_ele)
                heapq.heappush(k_min_ele, arr[i])
        return heapq.heappop(k_min_ele)


if __name__ == "__main__":
    arr = [3, 2, 1, 5, 6, 4]
    k = 2
    solu = Solution()
    res = solu.kth_largest_element(arr, k)
    print("The {}th largest element is {}.".format(k, res))
