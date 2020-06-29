import heapq


def smallest_k(array, k):
    if not array or len(array) <= 1:
        return array
    heapq.heapify(array)
    res = []
    for i in range(min(k, len(array))):
        res.append(heapq.heappop(array))
    return res


if __name__ == "__main__":
    a1 = [9, 2, 1, 4, 3, 6, 7]
    print("res1:", smallest_k(a1, 3))

    a2 = [7, 1, 2, 9, 10]
    print("res2:", smallest_k(a2, 2))

    a3 = []
    print("res3:", smallest_k(a3, 2))

    a4 = [7, 1, 2]
    print("res4:", smallest_k(a4, 4))

    a5 = [7]
    print("res5:", smallest_k(a5, 2))

