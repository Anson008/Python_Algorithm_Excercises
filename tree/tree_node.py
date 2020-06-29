class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.total_left = 0

    def _helper_pre_order(self, root, res):
        if not root:
            return
        res.append(root.val)
        self._helper_pre_order(root.left, res)
        self._helper_pre_order(root.right, res)

    def pre_order_traversal(self, root):
        res = []
        self._helper_pre_order(root, res)
        return res

    def _helper_in_order(self, root, res):
        if not root:
            return
        self._helper_in_order(root.left, res)
        res.append(root.val)
        self._helper_in_order(root.right, res)

    def in_order_traversal(self, root):
        res = []
        self._helper_in_order(root, res)
        return res

    def _helper_post_order(self, root, res):
        if not root:
            return
        self._helper_post_order(root.left, res)
        self._helper_post_order(root.right, res)
        res.append(root.val)

    def post_order_traversal(self, root):
        res = []
        self._helper_post_order(root, res)
        return res

    def get_height(self, root):
        if not root:
            return 0
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        return 1 + max(left, right)

    def get_size(self, root):
        if not root:
            return 0
        left = self.get_size(root.left)
        right = self.get_size(root.right)
        return 1 + left + right

    def get_num_nodes(self, node):
        if not node:
            return 0
        left_total = self.get_num_nodes(node.left)
        right_total = self.get_num_nodes(node.right)
        node.total_left = left_total
        return 1 + left_total + right_total

    def print_level(self, root):
        q = [root]  # current level
        next_level = []  # next level
        line = []  # content to print
        while q:
            head = q.pop(0)
            if head.left:
                next_level.append(head.left)
            if head.right:
                next_level.append(head.right)
            line.append(head.val)
            if not q:
                print(line)
                if next_level:
                    q = next_level
                    next_level = []
                    line = []


def flip(root):
    if not root:
        return root
    if not root.left and not root.right:
        return root
    prev, curr = None, root
    prev_right = None
    while curr:
        curr_left = curr.left
        curr_right = curr.right
        curr.right = prev
        curr.left = prev_right
        prev_right = curr_right
        prev = curr
        curr = curr_left
    return prev


if __name__ == "__main__":
    node1 = TreeNode(4)

    node2 = TreeNode(2)
    node3 = TreeNode(6)

    node4 = TreeNode(1)
    node5 = TreeNode(3)
    node6 = TreeNode(5)
    node7 = TreeNode(7)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    node3.left = node6
    node3.right = node7

    pre_order = node1.pre_order_traversal(node1)
    print("Pre-order:", pre_order)

    in_order = node1.in_order_traversal(node1)
    print("In-order:", in_order)

    post_order = node1.post_order_traversal(node1)
    print("Post-order:", post_order)

    height = node1.get_height(node2)
    print("Height:", height)

    node1.print_level(node1)

    # test flip()
    root = TreeNode(1)
    node11 = TreeNode(2)
    node12 = TreeNode(3)
    node21 = TreeNode(4)
    node22 = TreeNode(5)

    root.left = node11
    root.right = node12
    node11.left = node21
    node11.right = node22

    root.print_level(root)
    flipped_tree = flip(root)
    flipped_tree.print_level(flipped_tree)