def solution(A):
    # write your code in Python 3.6
    if len(A) <= 2:
        return A
    count_zero = 0
    while count_zero != len(A) - 2:
        i = 0
        count_zero = 0
        while i < len(A) - 1:
            if A[i - 1] < A[i] and A[i + 1] < A[i]:
                A[i] -= 1
            elif A[i - 1] > A[i] and A[i + 1] > A[i]:
                A[i] += 1
            else:
                count_zero += 1
            i += 1
    return A


l1 = [1, 6, 3, 5, 4, 4, 1]
l2 = [1, 0, 1]
print(solution(l1))
print(solution(l2))