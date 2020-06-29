def remove_duplicated(string):
    if not string or len(string) <= 1:
        return string
    lst = list(string)
    i, j = 1, 1
    while j < len(lst):
        if lst[j] != lst[i - 1]:
            lst[i] = lst[j]
            i += 1
        j += 1
    return ''.join(lst[:i])


if __name__ == "__main__":
    s1 = "aaabbbccddcc"
    print("res1:", remove_duplicated(s1))

    s2 = "aaabbbaaa"
    print("res2:", remove_duplicated(s2))

    s3 = ""
    print("res3:", remove_duplicated(s3))

    s4 = "abcccc"
    print("res4:", remove_duplicated(s4))

    s5 = "aaaabcd"
    print("res5:", remove_duplicated(s5))

    s6 = "a"
    print("res6:", remove_duplicated(s6))

    s7 = "aa"
    print("res7:", remove_duplicated(s7))