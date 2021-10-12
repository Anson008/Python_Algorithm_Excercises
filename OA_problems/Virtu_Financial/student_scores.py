def solution(A):
    # write your code in Python 3.6
    if len(A) <= 2:
        return A
    change = [0 for x in range(len(A))]
    count_zero = 0
    while count_zero != len(A) - 2:
        i = 1
        while i < len(A) - 1:
            if A[i - 1] < A[i] and A[i + 1] < A[i]:
                change[i] = -1
            elif A[i - 1] > A[i] and A[i + 1] > A[i]:
                change[i] = 1
            else:
                change[i] = 0
                count_zero += 1
            i += 1
        j = 0
        while j <= len(change) - 1:
            A[j] += change[j]
            j += 1
    return A