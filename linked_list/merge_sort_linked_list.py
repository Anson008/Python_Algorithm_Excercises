class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Soltion(object):
    def split_in_half(self, head):
        """
        Split a given linked list in two halves.
        :param head: ListNode head
        :return: ListNode
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        return head, head2

    def merge(self, one, two):
        """
        Merge two sorted link list.
        :param one: ListNode
        :param two: ListNode
        :return: ListNode
        """
        prev = ListNode(None)
        curr = prev
        while one and two:
            if one.val < two.val:
                curr.next = one
                one = one.next
            else:
                curr.next = two
                two = two.next
            curr = curr.next
        if one:
            curr.next = one
        else:
            curr.next = two
        return prev.next

    def merge_sort(self, head):
        """
        Merge sort of a singly linked list.
        :param head: ListNode head
        :return: ListNode
        """
        if not head or not head.next:
            return head
        one, two = self.split_in_half(head)
        one = self.merge_sort(one)
        two = self.merge_sort(two)
        return self.merge(one, two)
