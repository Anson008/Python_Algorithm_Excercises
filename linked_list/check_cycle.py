class _ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

    def __eq__(self, other):
        return isinstance(other, _ListNode) and other.val == self.val


class Solution:
    @staticmethod
    def check_cycle(head):
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

