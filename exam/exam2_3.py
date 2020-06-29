from tree.tree_node import TreeNode


def second_largest(root):
    if not root:
        return None
    if not root.right:
        return second_largest(root.left) or root.left
    else:
        return second_largest(root.right) or root


# Solution
class Solution(object):
    def find_largest(self, root):
        if not root:
            return None
        if not root.right:
            return root
        return self.find_largest(root.right)

    def find_2nd_largest(self, root):
        if not root:
            return None
        if not root.right:
            return self.find_largest(root.left)
        right = root.right
        if not right.left and not right.right:
            return root
        return self.find_2nd_largest(root.right)


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    print("res1:", second_largest(root).val)


    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.right.right = TreeNode(14)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(7)
    root.right.right.left = TreeNode(13)
    print("res2:", second_largest(root).val)
