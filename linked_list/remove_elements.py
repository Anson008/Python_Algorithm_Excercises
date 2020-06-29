class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


class Solution:
    @staticmethod
    def remove_elements1(head, val):
        fake_head = ListNode(None)
        fake_head.next = head
        prev = fake_head
        curr = head
        while curr:
            if curr.val != val:
                prev.next = curr
                prev = curr
            curr = curr.next
        prev.next = None
        return fake_head.next

    @staticmethod
    def remove_elements2(head, target):
        fake_head = ListNode(None)
        fake_head.next = head
        prev = fake_head
        curr = head
        while curr:
            if curr.val == target:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return fake_head.next

