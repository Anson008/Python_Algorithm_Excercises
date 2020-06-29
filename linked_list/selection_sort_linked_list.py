class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    @staticmethod
    def selection_sort(head):
        """
        Selection sort of a singly linked list.
        :param head:
        :return:
        """
        new_head = ListNode(None)
        new_head.next = head
        tail = new_head
        while tail.next:
            prev, curr = tail, tail.next
            min_node, min_node_predecessor = curr, prev
            while curr:
                if curr.val < min_node.val:
                    min_node, min_node_predecessor = curr, prev
                prev, curr = curr, curr.next
            min_node_predecessor.next = min_node.next
            next_node = tail.next
            tail.next = min_node
            min_node.next = next_node
            tail = tail.next
        return new_head.next
