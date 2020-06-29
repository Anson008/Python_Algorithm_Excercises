def get_height(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    left = get_height(root.left) if root.left else float("inf")
    right = get_height(root.right) if root.right else float("inf")
    return min(left, right) + 1

# Time: O(n)
# Space: O(log(n))
