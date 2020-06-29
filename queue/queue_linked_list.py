class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue(object):
    def __init__(self):
        """
        Initialize the queue by specifying the size, head and tail of the queue.
        """
        self.__size = 0
        self.__head, self.__tail = None, None

    def __len__(self):
        """
        return the length of the queue.
        :return: int
        """
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def enqueue(self, value):
        if not self.is_empty():
            self.__tail.next = ListNode(value)
            self.__tail = self.__tail.next
        else:
            self.__head = self.__tail = ListNode(value)
        self.__size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.__head.value
        self.__head = self.__head.next
        if not self.__head:
            self.__tail = None
        self.__size -= 1
        return value

    def front(self):
        if self.is_empty():
            return None
        return self.__head.value


