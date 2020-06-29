class _ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.head always refers to the head node of the internal singly linked list
        self._head = None

        # self.size is always the number of nodes inside the list.
        self._size = 0

        # self.tail always refers to the tail node of the list.
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
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :param index: int
        :return: int
        """
        if index < 0 or index >= self._size:
            return -1
        return self._get(index).val

    def add_at_head(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will
        be the first node of the linked list.
        :param val: int
        :return: None
        """
        if self._size == 0:
            self._head = self._tail = _ListNode(val)
        else:
            new_head = _ListNode(val)
            new_head.next = self._head
            self._head = new_head
        self._size += 1

    def add_at_tail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :param val: int
        :return: None
        """
        if self._size == 0:
            self._head = self._tail = _ListNode(val)
        else:
            self._tail.next = _ListNode(val)
            self._tail = self._tail.next
        self._size += 1

    def add_at_index(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to
        the length of linked list, the node will be appended to the end of linked list. If index
        is greater than the length, the node will not be inserted.
        :param index: int
        :param val: int
        :return: None
        """
        if index < 0 or index >= self._size:
            return
        if index == 0:
            self.add_at_head(val)
        elif index == self._size:
            self.add_at_tail(val)
        else:
            node = self._get(index - 1)
            new_node = _ListNode(val)
            new_node.next = node.next
            node.next = new_node
            self._size += 1

    def delete_at_index(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :param index: int
        :return: None
        """
        if index < 0 or index >= self._size:
            return
        if index == 0:
            new_head = self._head.next
            self._head.next = None
            self._head = new_head
            if self._head is None:
                self._tail = None
        else:
            node = self._get(index - 1)
            remove_node = node.next
            node.next = remove_node.next
            remove_node.next = None
            if index == self._size - 1:
                self._tail = node
        self._size -= 1

    def __str__(self):
        strs = []
        node = self._head
        while node is not None:
            strs.append(str(node.val))
            node = node.next
        return "->".join(strs)
