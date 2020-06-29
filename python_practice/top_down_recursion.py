class GetHeight(object):
    def find_height(self, root):
        if root is None:
            return 0
        self.result = 0
        self.helper(root, 0)
        return self.result

    def helper(self, root, depth):
        if root is None:
            self.result = max(self.result, depth)
            return

        self.helper(root.left, depth + 1)
        self.helper(root.right, depth + 1)
        return


class MinDepth(object):
    def min_depth(self, root):
        if root is None:
            return 0
        self.ret = float("inf")
        self.helper(root, 0)
        return self.ret

    def helper(self, root, depth):
        if root is None:
            return
        if root.left is None and root.right is None:
            self.ret = min(self.ret, depth + 1)
            return

        self.helper(root.left, depth + 1)
        self.helper(root.right, depth + 1)
        return


class MaxDepth(object):
    def max_depth(self, root):
        if root is None:
            return 0
        self.max = 0
        self.helper(root, 0)
        return self.max

    def helper(self, root, depth):
        if root is None:
            return
        if root.left is None and root.right is None:
            self.max = max(self.max, depth + 1)
            return

        self.helper(root.left, depth + 1)
        self.helper(root.right, depth + 1)
        return
    