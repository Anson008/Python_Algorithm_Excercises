def lowest_common_ancestor(root, p, q):
    if not root:
        return root
    if root == p or root == q:
        return root
    ltree = lowest_common_ancestor(root.left, p, q)
    rtree = lowest_common_ancestor(root.right, p, q)
    if ltree and rtree:
        return root
    elif not ltree:
        return rtree
    else:
        return ltree
