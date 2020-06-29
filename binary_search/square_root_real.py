def suqare_root_real(x, eps=1e-3):
    left, right = 1.0, x * 1.0
    if x < 1.0:
        left, right = x*1.0, 1.0
    while abs(left - right) > eps:
        mid = 0.5 * (left + right)
        midsq = mid * mid
        if abs(midsq - x) <= eps:
            return mid
        elif midsq > x:
            right = mid
        else:
            left = mid
    return left


if __name__ == "__main__":
    res1 = suqare_root_real(2.5)
    print(res1)

