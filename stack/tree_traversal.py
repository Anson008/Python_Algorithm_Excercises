class TreeNode(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def pre_order(root):
    current = root
    s = []
    done = False
    res = []
    while not done:
        if current:
            s.append(current)
            res.append(current.value)
            current = current.left
        else:
            if len(s) > 0:
                current = s.pop()
                current = current.right
            else:
                done = True
    return res


def in_order1(root):
    current = root
    s = []
    done = False
    res = []

    while not done:
        if current:
            s.append(current)
            current = current.left
        else:
            if len(s) > 0:
                current = s.pop()
                res.append(current.value)
                current = current.right
            else:
                done = True
    return res


def post_order(root):
    if not root:
        return
    s1 = []
    s2 = []
    res = []
    s1.append(root)

    while s1:
        node = s1.pop()
        s2.append(node)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)

    while s2:
        res.append(s2.pop().value)
    return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Pre-order:", pre_order(root))
    print("In-order:", in_order1(root))
    print("Post-order:", post_order(root))

    root1 = TreeNode(None)
    print(in_order1(root1))
