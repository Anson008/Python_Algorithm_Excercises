class DoublelyLinkedListNode:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.val = value


class Solution:
    def __init__(self):
        # Initialize the class.
        self.ch_to_node = {}
        self.head = DoublelyLinkedListNode(None)
        self.tail = DoublelyLinkedListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def read(self, ch):
        # Implement this method here.
        if ch in self.ch_to_node:
          remove_node = self.ch_to_node[ch]
          if remove_node is None:
            return
          remove_node.prev.next = remove_node.next
          remove_node.next.prev = remove_node.prev
          self.ch_to_node[ch] = None
          return
        node = DoublelyLinkedListNode(ch)
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node
        self.ch_to_node[ch] = node

    def first_non_repeat(self):
        # Implement this method here.
        return self.head.next.val