class Queue1(object):
    def __init__(self):
        """
        Initialize the internal to become a valid empty queue.
        """
        self.__items = []

    def __len__(self):
        """
        Return the number of items that are shared in the queue.
        :return: int
        """
        return len(self.__items)

    def enqueue(self, item):
        """
        Put item into the queue
        :param item: item to put in
        """
        self.__items.append(item)

    def dequeue(self):
        """
        Return the item that has been in the queue for the longest time and remove it.
        If queue is empty, None will be returned instead.
        :return: item in the queue
        """
        if self.is_empty():
            return None
        item = self.__items[0]
        del self.__items[0]
        return item

    def is_empty(self):
        """
        Return ture if the queue is empty, false otherwise.
        :return: boolean
        """
        return len(self.__items) == 0

    def front(self):
        """
        Return the item that has been in the queue for the longest time without removing it.
        If queue is empty, None will be returned instead.
        :return: item in the queue
        """
        if self.is_empty():
            return None
        return self.__items[0]


class Queue2(object):
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)


