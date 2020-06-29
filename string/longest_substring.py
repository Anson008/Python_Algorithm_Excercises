def length_of_longest_substring(string):
    max_length = 0
    hashS = dict()
    l = 0
    for r in range(0, len(string)):
        hashS[string[r]] = hashS.get(string[r], 0) + 1
        while l < len(string) and hashS[string[r]] > 1:
            hashS[string[l]] -= 1
            l += 1
        max_length = max(max_length, r - l + 1)
    return max_length

