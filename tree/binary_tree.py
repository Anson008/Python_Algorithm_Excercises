class _TreeNode(object):
    def __init__(self, key, value):
        """
        Initialize a tree node with a {key: value} pair.
        :param key: comparable type
        :param value: any type
        """
        self.key = key
        self.val = value
        self.left = None
        self.right = None
        self.total_left = 0
        self.total_right = 0


class BinaryTree:
    def __init__(self):
        self._root = None
        self._size = 0
        self._height = 0

    def set_root(self, key=None, value=None):
        """
        Set root node with key and value.
        :param key: comparable type
        :param value: any type
        """
        if not self._root:
            self._root = _TreeNode(key, value)
        else:
            self._root.key = key
            self._root.val = value

    def get_root(self):
        return self._root

    @staticmethod
    def set_node(node, key=None, value=None):
        """
        Set key and value for an existing node.
        :param node: _TreeNode, node to be set
        :param key: comparable type
        :param value: any type
        """
        node.key = key
        node.val = value

    def insert_left(self, node, key=None, value=None):
        """
        Insert a node to the existing binary tree as the left child of other.
        :param node: _TreeNode, the node to which a left child is inserted.
        :param key: comparable type
        :param value: any type
        """
        if node and not node.left:
            node.left = _TreeNode(key, value)
        else:
            t = _TreeNode(key, value)
            t.left = node.left
            node.left = t
        self._size += 1
        self._height += 1

    def get_left(self, node):
        return node.left

    def insert_right(self, node, key=None, value=None):
        """
        Insert a node to the existing binary tree as the right child of other.
        :param node: _TreeNode, the node to which a right child is inserted.
        :param key: comparable type
        :param value: any type
        """
        if not node.right:
            node.right = _TreeNode(key, value)
        else:
            t = _TreeNode(key, value)
            t.right = node.right
            node.right = t
        self._size += 1
        self._height += 1

    def get_right(self, node):
        return node.right

    def get_size(self, node):
        """
        Return the total number of nodes
        :param other: node from which the size is counted.
        """
        if not node:
            return 0
        left_total = self.get_size(node.left)
        right_total = self.get_size(node.right)
        node.total_left = left_total
        node.total_right = right_total
        return 1 + left_total + right_total

    def get_height(self, node):
        if not node:
            return 0
        left = self.get_height(node.left)
        right = self.get_height(node.right)
        return 1 + max(left, right)

    def _pre_order_helper(self, node, res):
        if not node:
            return
        res.append(node.key)
        self._pre_order_helper(node.left, res)
        self._pre_order_helper(node.right, res)

    def pre_order_traversal(self, node):
        res = []
        self._pre_order_helper(node, res)
        return res

    def _in_order_helper(self, node, res):
        if not node:
            return
        self._in_order_helper(node.left, res)
        res.append(node.key)
        self._in_order_helper(node.right, res)

    def in_order_traversal(self, node):
        res = []
        self._in_order_helper(node, res)
        return res

    def _post_order_helper(self, node, res):
        if not node:
            return
        self._post_order_helper(node.left, res)
        self._post_order_helper(node.right, res)
        res.append(node.key)

    def post_order_traversal(self, node):
        res = []
        self._post_order_helper(node, res)
        return res

    def _is_balanced_helper(self, node):
        if not node:
            return 0
        left = self._is_balanced_helper(node.left)
        right = self._is_balanced_helper(node.right)
        if left == -1 or right == -1:
            return False
        elif abs(left - right) > 1:
            return -1
        else:
            return 1 + max(left, right)

    def is_balanced(self, node):
        if self._is_balanced_helper(node) == -1:
            return False
        else:
            return True

    def is_symmetric(self, node):
        if not node:
            return True
        in_order = self.in_order_traversal(node)
        length = len(in_order)
        i = 0
        while i <= length // 2:
            if in_order[i] != in_order[length - 1 - i]:
                return False
            i += 1
        return True


if __name__ == "__main__":
    # Create a new tree
    my_BT = BinaryTree()
    my_BT.set_root(1, "a")
    root = my_BT.get_root()
    print("Root: ({}, {})".format(root.key, root.val))

    # Create children for root
    my_BT.insert_left(root, 2, "b")
    my_BT.insert_right(root, 3, "c")
    root_left = my_BT.get_left(root)
    root_right = my_BT.get_right(root)
    print("Root left: ({}, {})".format(root_left.key, root_left.val))
    print("Root right: ({}, {})".format(root_right.key, root_right.val))
    print("Size:", my_BT.get_size(root))
    print("Height:", my_BT.get_height(root))

    # Create left child for root.left
    my_BT.insert_left(root_left, 4, "d")
    root_left_left = my_BT.get_left(root_left)
    print("Root left left: ({}, {})".format(root_left_left.key, root_left_left.val))
    print("Size:", my_BT.get_size(root))
    print("Height:", my_BT.get_height(root))
    print("Total left of root:", root.total_left)
    print("Total right of root:", root.total_right)
    print("Total left of root_left:", root_left.total_left)
    print("Total right of root_right:", root_right.total_right)

    # traversal
    print("Pre-order:", my_BT.pre_order_traversal(root))
    print("In-order:", my_BT.in_order_traversal(root))
    print("Post-order:", my_BT.post_order_traversal(root))

    # Check balance
    print("Is balanced?", my_BT.is_balanced(root))

    # Check symmetry
    print("Is symmetric?", my_BT.is_symmetric(root))


