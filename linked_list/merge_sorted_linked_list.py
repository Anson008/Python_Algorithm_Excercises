class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def merge1(self, one, two):
        """
        :param one: ListNode one
        :param two: ListNode two
        :return: ListNode
        """
        if not one:
            return two
        if not two:
            return one
        if one.val > two.val:
            one, two = two, one
        one.next = self.merge1(one.next, two)
        return one

    def merge2(self, one, two):
        """
        :param one: ListNode one
        :param two: ListNode two
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


