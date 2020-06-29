from tree.tree_node import TreeNode

global_max = -1
res = None


def node_diff(root):
    if not root:
        return 0
    left_total = node_diff(root.left)
    right_total = node_diff(root.right)
    global global_max
    global res
    diff = abs(left_total - right_total)
    if diff > global_max:
        global_max = diff
        res = root
    return left_total + right_total + 1


def get_max_diff(root):
    global global_max
    global res
    node_diff(root)
    return res


if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(5)
    root.right.right.right = TreeNode(6)

    max_diff = get_max_diff(root)
    print(max_diff.val)
