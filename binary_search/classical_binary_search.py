def binary_search(array, target):
    """
    :param array: list
    :param target: int
    :return: int. If target is in array, return index of target. If not, return -1.
    """
    if not array:
        return -1
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] > target:
            right = mid - 1
        elif array[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1


def binary_search_2d(matrix, target):
    """
    :param matrix: list. 2D
    :param target: int
    :return: int
    """
    if not matrix:
        return -1
    nrow, ncol = len(matrix), len(matrix[0])
    left = 0
    right = nrow * ncol - 1
    while left <= right:
        mid = (left + right) // 2
        i = mid // ncol
        j = mid % ncol
        if matrix[i][j] < target:
            left = mid + 1
        elif matrix[i][j] > target:
            right = mid - 1
        else:
            return [i, j]
    return -1


def closest_element(array, target):
    if len(array) == 0:
        return -1
    left = 0
    right = len(array) - 1
    while left < right - 1:
        mid = (right + left) // 2
        if array[mid] < target:
            left = mid
        elif array[mid] > target:
            right = mid
        else:
            return mid
    return left if abs(array[left] - target) < abs(array[right] - target) else right


def find_first_occurrence(array, target):
    if not array:
        return -1
    left = 0
    right = len(array) - 1
    while left < right - 1:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            right = mid
    if array[left] == target:
        return left
    if array[right] == target:
        return right
    return -1


def find_last_occurrence(array, target):
    if not array:
        return -1
    left = 0
    right = len(array) - 1
    while left < right - 1:
        mid = (left + right) // 2
        if array[mid] > target:
            right = mid - 1
        elif array[mid] < target:
            left = mid + 1
        else:
            left = mid
    if array[right] == target:
        return right
    if array[left] == target:
        return left
    return -1


def total_occurrence(array, target):
    first = find_first_occurrence(array, target)
    last = find_last_occurrence(array, target)

    if first == -1:
        return 0
    else:
        return last - first + 1


def k_closest(array, target, k):
    if not array:
        return -1
    res = []
    if 0 <= k <= len(array):
        for i in range(k):
            index = closest_element(array, target)
            res.append(array[index])
            del array[index]
        return res
    else:
        return -1


def print_result(x):
    if x == -1:
        print("Not found.")
    else:
        print("Index:", x)


if __name__ == "__main__":
    # classical binary search
    a1 = [1, 3, 4, 6, 7, 8, 9, 18, 38, 52]
    a2 = []
    a3 = [1, 2]
    a4 = [2, 3, 5]
    print("-" * 40)
    print("Classical binary search test results:")
    print_result(binary_search(a1, 6))
    print_result(binary_search(a2, 6))
    print_result(binary_search(a3, 1))
    print_result(binary_search(a4, 6))

    # 2D binary search
    b1 = [[1, 2, 3], [4, 5, 6], [3, 5, 9]]
    b2 = [[]]
    print("-" * 40)
    print("2D binary search test results:")
    print_result(binary_search_2d(b1, 2))
    print_result(binary_search_2d(b2, 2))
    print_result(binary_search_2d(b1, 14))

    # closest element
    c1 = [1, 3, 5, 6, 9]
    print("-" * 40)
    print("Closest element test results:")
    print_result(closest_element(c1, 1))
    print_result(closest_element(c1, 3))
    print_result(closest_element(c1, 7))
