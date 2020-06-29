def sum_of_n_integers(n):
    if n == 1:
        return 1
    return sum_of_n_integers(n - 1) + n


def print_linked_list(head):
    if not head:
        return
    print(head.value)
    print(head.next)


def reverse(head):
    if not head or not head.next:
        return head
    new_head = reverse(head.next)
    head.next.next = head
    head.next = None
    return new_head


def list_sum(array):
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + list_sum(array[1:])


def int_to_string(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return int_to_string(n // base, base) + convert_string[n % base]


if __name__ == "__main__":
    a1 = [1, 2, 3, 4]
    print("Sum of a1:", list_sum(a1))
