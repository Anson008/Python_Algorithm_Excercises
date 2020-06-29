from tree.tree_node import TreeNode


class Solution11(object):
    def in_order(self, root, result):
        if not root:
            return
        self.in_order(root.left, result)
        result.append(root.val)
        self.in_order(root.right, result)

    def is_BST(self, root):
        result = []
        self.in_order(root, result)
        for i in range(len(result) - 1):
            if result[i] >= result[i + 1]:
                return False
        return True


class Solution12(object):
    def in_order(self, root, result):
        if not root:
            return True
        if not self.in_order(root.left, result):
            return False
        if len(result) > 0 and result[-1] >= root.val:
            return False
        else:
            result.append(root.val)
        if not self.in_order(root.right, result):
            return False
        return True

    def is_BST(self, root):
        result = []
        return self.in_order(root, result)


INT_MIN = -float('inf')


class Solution13(object):
    def in_order(self, root, prev):
        if not root:
            return True
        if not self.in_order(root.left, prev):
            return False
        if prev[0] >= root.val:
            return False
        prev[0] = root.val
        if not self.in_order(root.right, prev):
            return False
        return True

    def is_BST(self, root):
        prev = [INT_MIN]
        return self.in_order(root, prev)


class Solution21(object):
    def is_bst(self, root):
        return self.is_bst_util(root, -float('inf'), float('inf'))

    def is_bst_util(self, root, mini, maxi):
        if not root:
            return True
        if not (mini <= root.val <= maxi):
            return False
        return self.is_bst_util(root.left, mini, root.val - 1) and \
               self.is_bst_util(root.right, root.val + 1, maxi)


class Solution22(object):
    def is_bst(self, root):
        return self.is_bst_util(root, -float('inf'), float('inf'))

    def is_bst_util(self, root, mini, maxi):
        if not root:
            return True
        if not (mini < root.val < maxi):
            return False
        return self.is_bst_util(root.left, mini, root.val) and \
               self.is_bst_util(root.right, root.val, maxi)


class Solution3(object):
    def helper(self, root):
        if not root:
            return True, None, None
        lr, lmin, lmax = self.helper(root.left)
        rr, rmin, rmax = self.helper(root.right)
        return lr and rr and (not lmax or lmax < root.val) \
               and (not rmin or rmin > root.val), lmin or root.val, rmax or root.val

    def is_bst(self, root):
        return self.helper(root)[0]


if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    #root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    print(root.in_order_traversal(root))

    solu11 = Solution11()
    print("Solution 11:", solu11.is_BST(root))

    solu12 = Solution12()
    print("Solution 12:", solu12.is_BST(root))

    solu13 = Solution13()
    print("Solution 13:", solu13.is_BST(root))

    solu21 = Solution21()
    print("Solution 21:", solu21.is_bst(root))

    solu22 = Solution22()
    print("Solution 22:", solu22.is_bst(root))

    solu3 = Solution3()
    print("Solution 3:", solu3.is_bst(root))