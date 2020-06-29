def longest(curr, parent, currlen):
    if not curr:
        return currlen
    size = 1
    if parent and curr.val == parent.val + 1:
        size = currlen + 1
    return max(currlen, longest(curr.left, curr, size), longest(curr.right, curr, size))

# time: O(n)
