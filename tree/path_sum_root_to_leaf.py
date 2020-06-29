class Solution1(object):
    def has_path_sum(self, root, sum):
        self.sum = sum
        self.ret = False
        self.helper(root, 0)
        return self.ret

    def helper(self, root, current):
        if root is None:
            return
        if not root.left and not root.right:
            self.ret = self.ret or (current + root.val == self.sum)
        self.helper(root.left, current + root.val)
        self.helper(root.right, current + root.val)
        return


class Solution2(object):
    def has_path_sum(self, root, sum):
        self.sum = sum
        return self.helper(root, 0)

    def helper(self, root, current):
        if root is None:
            return False
        if not root.left and not root.right:
            return current + root.val == self.sum
        return self.helper(root.left, current + root.val) or self.helper(root.right, current + root.val)


class Solution3(object):
    def has_path_sum(self, root, sum):
        self.sum = sum
        self.ret = 0
        if not root:
            return False
        self.helper(root, root.val)
        return self.ret

    def helper(self, root, current):
        if not root:
            return
        if not root.left and not root.right:
            self.ret = self.ret or (current == self.sum)
        if root.left:
            self.helper(root.left, current + root.left.val)
        if root.right:
            self.helper(root.right, current + root.right.val)
        return