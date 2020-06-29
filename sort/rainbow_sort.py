def rainbow_sort(array):
    curr = 0
    left = 0
    right = len(array) - 1
    while curr <= right:
        if array[curr] == 0:
            curr += 1
        elif array[curr] == 1:
            array[curr], array[right] = array[right], array[curr]
            right -= 1
        else:
            array[curr], array[left] = array[left], array[curr]
            curr += 1
            left += 1
    return array


a1 = [1, 0, 1, 0, 0, -1, 1, -1]
print(rainbow_sort(a1))