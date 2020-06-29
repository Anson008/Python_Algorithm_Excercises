class Solution:
    def is_identical(self, one, two):
        if one is None or two is None:
            return False
        if one is None and two is None:
            return True
        return one.val == two.val and self.is_identical(one.left, two.left) and self.is_identical(one.right, two.right)

