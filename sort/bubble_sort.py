def bubble_sort_1(lst):
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def bubble_sort_2(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def bubble_sort_3(lst):
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i, 0, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]


def bubble_sort_4(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i, 0, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]


def short_bubble_sort(array):
    exchange = True
    pass_num = len(array) - 1
    while pass_num > 0 and exchange:
        exchange = False
        for i in range(pass_num):
            if array[i] > array[i + 1]:
                exchange = True
                array[i], array[i + 1] = array[i + 1], array[i]
        pass_num -= 1


if __name__ == "__main__":
    a1 = [3, 2, 9, 6, 34, 23, 87]
    print("Original:", a1)
    bubble_sort_4(a1)
    print("Sorted:", a1)
