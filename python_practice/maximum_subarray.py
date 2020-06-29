def max_subarray(array, left, right):
    if left == right:
        return array[left]
    center = (left + right) // 2
    max_left_sum = max_subarray(array, left, center)
    max_right_sum = max_subarray(array, center + 1, right)
    max_center_sum = get_max_center_sum(array, center, left, right)
    max_sum = max(max_left_sum, max_right_sum, max_center_sum)
    return max_sum


def get_max_center_sum(array, center, left, right):
    max_left_border_sum = -float('inf')
    left_border_sum = 0
    for i in range(center, left - 1, -1):
        left_border_sum += array[i]
        max_left_border_sum = max(left_border_sum, max_left_border_sum)

    max_right_border_sum = -float('inf')
    right_border_sum = 0
    for i in range(center + 1, right + 1):
        right_border_sum += array[i]
        max_right_border_sum = max(right_border_sum, max_right_border_sum)
    return max_left_border_sum + max_right_border_sum


def max_subarray_kadane(array):
    for i in range(1, len(array)):
        if array[i - 1] > 0:
            array[i] += array[i - 1]
    return max(array)


if __name__ == "__main__":
    a1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res1 = max_subarray_kadane(a1)
    print(res1)