import random


def partition(left, right, pivot_idx, arr):
    pivot = arr[pivot_idx]
    new_pivot_idx = left
    arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
    for i in range(left, right):
        if arr[i] > pivot:
            arr[i], arr[new_pivot_idx] = arr[new_pivot_idx], arr[i]
            new_pivot_idx += 1
    arr[right], arr[new_pivot_idx] = arr[new_pivot_idx], arr[right]
    return new_pivot_idx


def find_kth_largest(arr, k):
    left, right = 0, len(arr) - 1
    while left < right:
        pivot_idx = random.randint(left, right)
        new_pivot_idx = partition(left, right, pivot_idx, arr)
        if new_pivot_idx == k - 1:
            return arr[new_pivot_idx]
        elif new_pivot_idx > k - 1:
            right = new_pivot_idx - 1
        else:
            left = new_pivot_idx + 1

