class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def print_linked_list(node):
    while node:
        print(node.value)
        node = node.next
    print("#"*10)


def remove_vowels1(head):
    vowels = ['a', 'e', 'i', 'o', 'u']
    fake_head = ListNode(None)
    fake_head.next = head
    curr = fake_head
    while curr.next:
        if curr.next.value in vowels:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return fake_head.next


def remove_vowels2(head):
    vowels = ['a', 'e', 'i', 'o', 'u']
    fake_head = ListNode(None)
    fake_head.next = head
    prev = fake_head
    curr = head
    while curr:
        if curr.value in vowels:
            curr = curr.next
            prev.next = curr
        else:
            prev = curr
            curr = curr.next
    return fake_head.next

