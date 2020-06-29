def selection_sort_min(lst):
    if not lst:
        return None
    n = len(lst)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


def selection_sort_max1(lst):
    if not lst:
        return None
    n = len(lst)
    for i in range(n - 1, 0, -1):
        max_index = i
        for j in range(i - 1, -1, -1):
            if lst[j] > lst[max_index]:
                max_index = j
        lst[i], lst[max_index] = lst[max_index], lst[i]
    return lst


def selection_sort_max2(array):
    if not array:
        return None
    n = len(array)
    for i in range(n - 1, 0, -1):
        max_index = 0
        for j in range(i + 1):
            if array[j] > array[max_index]:
                max_index = j
        array[i], array[max_index] = array[max_index], array[i]
    return array


if __name__ == "__main__":
    list_unsorted = [32, 12, 4, 45, 56, 9]
    print("Unsorted list: ", list_unsorted)
    list_sorted = selection_sort_max2(list_unsorted)
    print("Sorted list: ", list_sorted)

