class ListNode(object):
    def __init__(self, value):
        self.next = None
        self.value = value

    def __eq__(self, other):
        return isinstance(other, ListNode) and self.value == other.value


def print_node(head):
    if head is None:
        print("None")
    else:
        print(head.value)


def print_all_nodes(head):
    curr = head
    while curr:
        print(curr.value)
        curr = curr.next


def search_by_index(head, index):
    """
    :param index: valid index >= 0
    :return: a node object if found, None othervise
    """
    if head is None or index < 0:
        return -1
    for i in range(index):
        head = head.next
        if not head:
            return None
    return head


def search_by_value(head, value):
    if not head:
        return None
    curr = head
    while curr:
        if curr.value == value:
            return curr
        curr = curr.next
    return None


def add_to_index(head, index, value):
    """
    :param head: type node, the first node of passed singly linked list
    :param index: type int, the position where you want to insert (starting from 0)
    :param value: type *, the value that will be referred by the newly added
    list node object if the operation is successful.
    :return: None
    """
    fake_head = ListNode(None)
    fake_head.next = head
    insert_place = search_by_index(fake_head, index)
    if insert_place is not None:
        new_node = ListNode(value)
        new_node.next = insert_place.next
        insert_place.next = new_node
    return fake_head.next


def remove_from_index(head, index):
    """

    :param head: type node, the first node of passed singly linked list
    :param index: type int, the position where you want to remove (starting from 0)
    :return: None
    """
    fake_head = ListNode(None)
    fake_head.next = head
    predecessor_remove_place = search_by_index(fake_head, index)
    if predecessor_remove_place is None:
        return fake_head.next
    remove_node = predecessor_remove_place.next
    predecessor_remove_place.next = remove_node.next
    remove_node.next = None
    return fake_head.next


node1 = ListNode("H")
node2 = ListNode("E")
node3 = ListNode("U")
node1.next = node2
node2.next = node3

# print_node(node3)
# print_all_nodes(node2)
print_node(search_by_index(node1, 2))
print_node(search_by_value(node1, "k"))
print_all_nodes(add_to_index(node1, 2, "W"))
print_all_nodes(remove_from_index(node1, 0))