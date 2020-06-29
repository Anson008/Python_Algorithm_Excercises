def insertion_sort1(array):
    for i in range(1, len(array)):
        current = array[i]
        j = i
        while j > 0 and current < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = current


def insert_num(array, n):
    idx = len(array) - 1
    array.append(n)
    while idx >= 0:
        if array[idx] > array[idx + 1]:
            array[idx + 1], array[idx] = array[idx], array[idx + 1]
        idx -= 1
    # print(array)


def insertion_sort2(array):
    new_arr = []
    for i in range(len(array)):
        insert_num(new_arr, array[i])
    return new_arr


def max_less_than(array, target):
    if not array:
        return 0
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
    if array[left] >= target:
        return left
    elif array[left] < target < array[right]:
        return right
    else:
        return right + 1


def insert_num3(arr, n):
    idx = len(arr) - 1
    insert_index = max_less_than(arr, n)
    arr.append(n)
    while idx >= insert_index:
        arr[idx + 1] = arr[idx]
        idx -= 1
    arr[insert_index] = n


def insertion_sort3(arr):
    if not arr:
        return []
    res = []
    for i in range(len(arr)):
        # insert_index = max_less_than(res, arr[i])
        # res.insert(insert_index, arr[i])
        insert_num3(res, arr[i])
    return res


if __name__ == "__main__":
    a1 = [1, 2, 3, 4]
    a2 = [4, 3, 2, 1]
    a3 = [2, 1, 4, 3]
    a4 = []
    a5 = [1]
    a6 = [8, 7, 4, 9, 18, 24, 1]
    a7 = [-1, -3, 0, 5, -8, -9.9]
    a_list = [a1, a2, a3, a4, a5, a6, a7]
    print("\ninsertion_sort2 results:")
    for a in a_list:
        print(insertion_sort2(a))
    print("\ninsertion_sort3 results:")
    for a in a_list:
        print(insertion_sort3(a))
    print("\ninsertion_sort1 results:")
    for a in a_list:
        insertion_sort1(a)
        print(a)

