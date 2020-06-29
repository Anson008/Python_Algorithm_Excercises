from linked_list.linked_list_node import ListNode


class Solution:
    @staticmethod
    def insert_sorted_linked_list(head, value):
        fake_head = ListNode(0)
        fake_head.next = head
        prev = fake_head
        while prev.next and prev.next.val < value:
            prev = prev.next
        new_node = ListNode(value)
        new_node.next = prev.next
        prev.next = new_node
        return fake_head.next
