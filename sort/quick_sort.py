from random import randrange


def partition(array, start, end, pivot_index):
    array[pivot_index], array[end] = array[end], array[pivot_index]
    store_index = start
    pivot = array[end]
    for i in range(start, end):
        if array[i] < pivot:
            array[store_index], array[i] = array[i], array[store_index]
            store_index += 1
    array[store_index], array[end] = array[end], array[store_index]
    return store_index


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot_index = randrange(start, end + 1)
    new_pivot_index = partition(array, start, end, pivot_index)
    quick_sort(array, start, new_pivot_index - 1)
    quick_sort(array, new_pivot_index + 1, end)

# time: average O(n*log(n)), worst O(n^2)
# space: average O(log(n)), worst O(n)


a1 = [28, 2, -1, 4]
print("Original:", a1)
quick_sort(a1, 0, len(a1) - 1)
print("Sorted:", a1)