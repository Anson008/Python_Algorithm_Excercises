from tree.tree_node import TreeNode


class Solution(object):
    def maxSumPath(self, root):
        if root.left is None and root.right is None:
            return root.value
        if root.left is None:
            return self.maxSumPath(root.right) + root.value
        if root.right is None:
            return self.maxSumPath(root.left) + root.value
        return max(self.maxSumPath(root.left), self.maxSumPath(root.right)) + root.value

