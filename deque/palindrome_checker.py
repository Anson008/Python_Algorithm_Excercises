from deque.my_deque import Deque


def pal_checker(string):
    char_deque = Deque()
    for char in string:
        char_deque.add_rear(char)
    equal = True
    while char_deque.size() > 1 and equal:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            equal = False
    return equal
        