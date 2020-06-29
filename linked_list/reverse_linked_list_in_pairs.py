from linked_list.linked_list_node import ListNode


def reverse_in_pairs(head):
    if not head or not head.next:
        return head
    dummy_node = ListNode(0)
    prev_node = dummy_node
    while head and head.next:
        next_node = head.next.next
        prev_node.next = head.next
        head.next.next = head
        head.next = next_node
        prev_node = head
        head = head.next
    return dummy_node.next

