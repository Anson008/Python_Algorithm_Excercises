import heapq


def smallest_range(arrays):
    """
    input: int[][] arrays
    return: int[]
    """
    # write your solution here
    heap = []
    k = len(arrays)
    upper = float("-inf")
    for i in range(len(arrays)):
        if len(arrays[i]):
            heap.append((arrays[i][0], i, 0))
            upper = max(arrays[i][0], upper)
    heapq.heapify(heap)
    result = [float("-inf"), float("inf")]
    while len(heap) == k:
        lower, index_array, index_element = heapq.heappop(heap)
        if upper - lower < result[1] - result[0]:
            result = [lower, upper]
        if index_element + 1 < len(arrays[index_array]):
            upper = max(upper, arrays[index_array][index_element + 1])
            heapq.heappush(heap, (arrays[index_array][index_element + 1], index_array, index_element + 1))
    return result
