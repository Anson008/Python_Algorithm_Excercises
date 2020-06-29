def merge(array1, array2):
    i = j = 0
    result = []
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1
    if i < len(array1):
        result.extend(array1[i:])
    if j < len(array2):
        result.extend(array2[j:])
    return result


def merge_sort(array):
    if len(array) == 0 or len(array) == 1:
        return array
    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    return merge(left, right)

# time: O(n*log(n))
# space: O(n)


if __name__ == "__main__":
    a1 = [3, 27, 38, 43]
    a2 = [3, 10, 82]
    m1 = merge(a1, a2)
    print("Merged array:", m1)

    a3 = [4, 1, 12, 45, 98, 12, 23]
    print("Unsorted:", a3)
    a3_sorted = merge_sort(a3)
    print("Sorted:", a3_sorted)
