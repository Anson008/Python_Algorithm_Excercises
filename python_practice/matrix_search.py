def matrix_search(arr, x):
    row, col = 0, len(arr[0]) - 1
    while row < len(arr) and col > 0:
        if arr[row][col] == x:
            return True
        elif arr[row][col] < x:
            row += 1
        else:
            col -= 1
    return False


if __name__ == "__main__":
    m1 = [[1, 2, 3, 4], [4, 6, 7, 8], [5, 9, 11, 13], [8, 10, 14, 17]]
    x = 14
    print("Have {}? {}".format(x, matrix_search(m1, x)))
