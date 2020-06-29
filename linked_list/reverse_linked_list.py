class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return self.val


class Solution(object):
    @staticmethod
    def reverse(head):
        """
        Given the head of a singly linked list, return the head of the reversed list.
        :param head: ListNode, head of the list
        :return: ListNode, head of the reversed list.
        """
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        return prev


if __name__ == "__main__":
    node1 = ListNode("E")
    node2 = ListNode("V")
    node3 = ListNode("A")
    node1.next = node2
    node2.next = node3
    node3.next = None

    solution = Solution()
    new_head = solution.reverse(node1)
    print(new_head, new_head.next, new_head.next.next)