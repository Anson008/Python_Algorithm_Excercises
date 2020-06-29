class ListNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None


def print_list(head):
    while head:
        print(head.value)
        head = head.next


def reverse_list(node):
    prev_node = None
    while node:
        next_node = node.next
        node.next = prev_node
        prev_node = node
        node = next_node
    return prev_node


def add_list(head1, head2):
    new_head1 = reverse_list(head1)
    new_head2 = reverse_list(head2)
    fake_head = ListNode("fake_head")
    cur_node = fake_head
    carry = 0
    while new_head1 and new_head2:
        temp_sum = new_head1.val + new_head2.val + carry
        carry = temp_sum // 10
        cur_node.next = ListNode(temp_sum % 10)
        cur_node = cur_node.next
        new_head1 = new_head1.next
        new_head2 = new_head2.next
    while new_head1:
        temp_sum = new_head1.val + carry
        carry = temp_sum // 10
        cur_node.next = ListNode(temp_sum % 10)
        cur_node = cur_node.next
        new_head1 = new_head1.next
    while new_head2:
        temp_sum = new_head2.val + carry
        carry = temp_sum // 10
        cur_node.next = ListNode(temp_sum % 10)
        cur_node = cur_node.next
        new_head2 = new_head2.next
    if carry > 0:
        cur_node.next = ListNode(carry)
    return reverse_list(fake_head.next)

# time: O(n)
# space: O(n)
