import heapq


def k_smallest1(array, k):
    if not array:
        return []
    res = []
    heapq.heapify(array)
    for i in range(min(k, len(array))):
        res.append(heapq.heappop(array))
    return res


def k_smallest2(array, k):
    if not array:
        return []
    if k >= len(array):
        return array
    res = [-elem for elem in array[0:k]]
    heapq.heapify(res)
    for i in range(k, len(array)):
        if array[i] < -res[0]:
            heapq.heappop(res)
            heapq.heappush(res, -array[i])
    return [-elem for elem in res]


if __name__ == "__main__":
    a1 = [4, 5, 10, 2, 0, 1, 3]
    res1 = k_smallest1(a1, 3)
    print(res1)

    a2 = [4, 5, 10, 2, 0, 1, 3]
    res2 = k_smallest2(a2, 3)
    print(res2)