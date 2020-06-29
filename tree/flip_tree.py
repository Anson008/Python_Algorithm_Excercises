class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def flip(root):
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
    root = TreeNode(1)
    node11 = TreeNode(2)
    node12 = TreeNode(3)
    node21 = TreeNode(4)
    node22 = TreeNode(5)

    root.left = node11
    root.right = node12
    node11.left = node21
    node11.right = node22





