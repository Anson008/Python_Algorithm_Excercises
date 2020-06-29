def sqrt_num1(n):
    """
    Return the largest integer whose square is less than or equal to the given integer.
    :param n: int, a non-negative integer
    :return: int
    """
    for i in range(1, n/2 + 1):
        if i ** 2 > n:
            return i - 1
    return n


def sqrt_num2(n):
    i = 1
    while i ** 2 <= n:
        i += 1
    return i - 1


def sqrt_num3(n):
    if n <= 1:
        return n
    left, right = 1, n // 2
    while left < right - 1:
        mid = (left + right) // 2
        mid_sq = mid ** 2
        if mid_sq == n:
            return mid
        elif mid_sq > n:
            right = mid
        else:
            left = mid
    if right ** 2 <= n:
        return right
    else:
        return left


if __name__ == "__main__":
    res = sqrt_num3(10)
    print(res)
