class _TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ret = 0

    def path_sum(self, root, target):
        hash = dict()
        self._helper(root, target, hash, 0)
        return self.ret > 0

    def _helper(self, root, target, hash, cur):
        if not root:
            return
        cur += root.val
        if cur == target:
            self.ret += 1
        if cur - target in hash:
            self.ret += hash[cur - target]
        if cur in hash:
            hash[cur] += 1
        else:
            hash[cur] = 1
        self._helper(root.left, target, hash, cur)
        self._helper(root.right, target, hash, cur)
        hash[cur] -= 1
        cur -= root.val
        return

