import heapq


def mergek(arrays):
    if not arrays:
        return None
    heap = []
    for i in range(len(arrays)):
        if len(arrays[i]):
            heap.append((arrays[i][0], i, 0))
    heapq.heapify(heap)
    result = []
    while heap:
        val, index_array, index_element = heapq.heappop(heap)
        result.append(val)
        if index_element + 1 < len(arrays[index_array]):
            heapq.heappush(heap, (arrays[index_array][index_element + 1], index_array, index_element + 1))
    return result


if __name__ == "__main__":
    a1 = [[1, 2, 3], [0, 4, 5], [-1, 6, 9]]
    res1 = mergek(a1)
    print(res1)
