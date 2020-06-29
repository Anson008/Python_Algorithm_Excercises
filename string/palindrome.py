class ListNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None


def print_all_node(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print("->".join(res))


def copy_list(head):
    fake_head = ListNode(None)
    curr_node = fake_head
    while head:
        curr_node.next = ListNode(head.val)
        curr_node = curr_node.next
        head = head.next
    return fake_head.next


def reverse(node):
    prev_node = None
    while node:
        next_node = node.next
        node.next = prev_node
        prev_node = node
        node = next_node
    return prev_node


def is_palindrome1(head):
    head1 = copy_list(head)
    head2 = reverse(head)
    while head1 and head2:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next
    return True

# time: O(n)
# Space: O(n)


def find_middle(head):
    if not head or not head.next:
        return head
    slow = head
    fast = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    return slow


def is_palindrome2(head):
    fake_head = ListNode(None)
    fake_head.next = head
    mid_node_prev = find_middle(fake_head)
    mid_node = mid_node_prev.next
    mid_node_prev.next = None
    head1 = head
    head2 = reverse(mid_node)
    while head1 and head2:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next
    return True


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(1)

    node1.next = node2
    node2.next = node3

    print_all_node(node1)

    print(is_palindrome1(node1))
