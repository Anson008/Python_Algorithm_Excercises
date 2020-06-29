from tree.tree_node import TreeNode


class Solution(object):
    @staticmethod
    def zigzag_level_order(root):
        if not root:
            return []
        curr_level = [root]
        ans = []
        reverse = False
        while curr_level:
            next_level, curr_val = [], []
            for u in curr_level:
                curr_val.append(u.val)
                if u.left:
                    next_level.append(u.left)
                if u.right:
                    next_level.append(u.right)
            ans.append(curr_val[::-1] if reverse else curr_val)
            curr_level = next_level
            reverse = not reverse
        return ans


if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(5)

    solu = Solution()
    print(solu.zigzag_level_order(root))
