class _TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    @staticmethod
    def pre_order_traverse(root):
        res = []
        if not root:
            return res
        stack = [(root, 1)]
        while stack:
            node, count = stack.pop()
            if count == 1:
                res.append(node.value)
                stack.append((node, count + 1))
                if node.left:
                    stack.append((node.left, 1))
            if count == 2:
                stack.append((node, count + 1))
                if node.right:
                    stack.append((node.right, 1))
        return res

    @staticmethod
    def in_order_traverse(root):
        res = []
        if not root:
            return res
        stack = [(root, 1)]
        while stack:
            node, count = stack.pop()
            if count == 1:
                stack.append((node, count + 1))
                if node.left:
                    stack.append((node.left, 1))
            if count == 2:
                res.append(node.value)
                stack.append((node, count + 1))
                if node.right:
                    stack.append((node.right, 1))
        return res

    @staticmethod
    def post_order_traverse(root):
        res = []
        if not root:
            return res
        stack = [(root, 1)]
        while stack:
            node, count = stack.pop()
            if count == 1:
                stack.append((node, count + 1))
                if node.left:
                    stack.append((node.left, 1))
            if count == 2:
                stack.append((node, count + 1))
                if node.right:
                    stack.append((node.right, 1))
            if count == 3:
                res.append(node.value)
                continue
        return res


if __name__ == "__main__":
    node0 = _TreeNode(1)
    node0.left = _TreeNode(2)
    node0.right = _TreeNode(3)
    pre_order = node0.pre_order_traverse(node0)
    print("Pre-order:", pre_order)
    in_order = node0.in_order_traverse(node0)
    print("In-order:", in_order)
    post_order = node0.post_order_traverse(node0)
    print("Post-order:", post_order)





