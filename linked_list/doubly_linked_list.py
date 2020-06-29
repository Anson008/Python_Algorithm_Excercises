class _ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class MyDoublyLinkedList(object):
    def __init__(self):
        """
        Initialize your data structure.
        """
        # self._head always refers to the head node of the internal doubly linked list.
        self._head = None

        # self._size is always the number of nodes inside the list.
        self._size = 0

        # self._tail always refers to the tail node of the list.
        self._tail = None

    def _get(self, index):
        """
        Assume index is in [0, self._size)
        :param index: int
        :return: node of the linked list
        """
        node = self._head
        for _ in range(index):
            node = node.next
        return node

    def get(self, index):
        """
        Get the value of index-th node in the linked list. If the index is invalid, return -1.
        :param index: int
        :return: int
        """
        if index < 0 or index >= self._size:
            return -1
        return self._get(index).value

    def add_at_head(self, val):
        pass

    def add_at_tail(self, val):
        pass

    def add_at_index(self, val):
        pass

    def delete_at_index(self, index):
        pass