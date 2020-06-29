class _Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        """
        Initialize the internal to become a valid empty binary search tree.
        """
        self._root = None

    def _insert(self, root, key, value):
        if not root:
            return _Node(key, value)
        if key < root.key:
            root.left = self._insert(root.left, key, value)
        elif key > root.key:
            root.right = self._insert(root.right, key, value)
        else:
            root.value = value
        return root

    def insert(self, key, value):
        """
        If key is in the tree, the associated value will be updated by input value.
        Otherwise, a new key value pair will be put into our tree.
        :param key:
        :param value:
        :return:
        """
        self._insert(self._root, key, value)

    def insert_iteratively(self, key, value):
        if not self._root:
            self._root = _Node(key, value)
            return
        curr, prev, is_left = self._root, None, None
        while curr:
            prev = curr
            if key < curr.key:
                is_left = True
                curr = curr.left
            elif key > curr.key:
                is_left = False
                curr = curr.right
            else:
                curr.value = value
                break

        if not curr:
            node = _Node(key, value)
            if is_left:
                prev.left = node
            else:
                prev.right = node

    def _query(self, root, key):
        if not root:
            return None
        if root.key == key:
            return root.value
        elif root.key < key:
            return self._query(root.right, key)
        else:
            return self._query(root.left, key)

    def query(self, key):
        """
        If key is in the tree, the associated value is returned.
        Otherwise, None is returned
        :param key:
        :return:
        """
        return self._query(self._root, key)

    def query_iterative(self, key):
        curr = self._root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return key.value
        return None

    def _min(self, root):
        if not root.left:
            return root
        return self._min(root.left)

    def _delete_min(self, root):
        if not root.left:
            return root.right
        root.left = self._delete_min(root.left)
        return root

    def _delete(self, root, key):
        if not root:
            return None
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            temp = root
            root = self._min(temp.right)
            root.right = self._delete_min(temp.right)
            root.left = temp.left
        return root

    def delete(self, key):
        """
        If key is in the tree, this key-value pair is removed.
        Otherwise, this function is a no-op
        :param key:
        :return:
        """
        self._root = self._delete(self._root, key)


def find_min(root):
    if not root:
        return None
    return find_min(root.left) or root


def find_max(root):
    if not root:
        return None
    return find_max(root.right) or root


def find_first_larger_than_target(root, target):
    if not root:
        return None
    if root.value == target:
        return find_min(root.right)
    elif root.value < target:
        return find_first_larger_than_target(root.right, target)
    else:
        return find_first_larger_than_target(root.left, target) or root


def find_last_smaller_than_target(root, target):
    if not root:
        return None
    if root.value == target:
        return find_max(root.left)
    elif root.value > target:
        return find_last_smaller_than_target(root.left, target)
    else:
        return find_last_smaller_than_target(root.right, target) or root


if __name__ == "__main__":
    pass




