from collections import deque
from tree.tree_node import TreeNode


class Solution(object):
    def level_order_1(self, root):
        """
        Traverse a binary tree in level order.
        :param root: tree node. Root of the tree.
        :return: list.
        """
        if not root:
            return []
        q = deque([root])
        result = []
        while q:
            node = q.popleft()
            result.append(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return result

    def level_order_2(self, root):
        """
        Traverse a binary tree in level order.
        :param root: tree node. Root of the tree.
        :return: list of lists.
        """
        if not root:
            return []
        q = deque([root])
        result = []
        while q:
            size = len(q)
            curr_level = []
            for _ in range(size):
                node = q.popleft()
                curr_level.append(node.value)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(curr_level)
        return result


