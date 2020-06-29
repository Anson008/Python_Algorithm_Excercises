def invert_tree1(root):
    if root is None:
        return None
    left = invert_tree1(root.left)
    right = invert_tree1(root.right)
    root.left, root.right = right, left
    return root


def invert_tree2(root):
    if root is None:
        return None
    root.left, root.right = root.right, root.left
    invert_tree2(root.left)
    invert_tree2(root.right)
    return root

