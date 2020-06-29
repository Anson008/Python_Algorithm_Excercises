class BinaryMinHeap:
    def __init__(self):
        """
        self.heap: list, list representation of a binary min heap
        self.size: int, current size of the binary min heap
        """
        self.heap = []
        self.size = 0

    def _percolate_up(self, i):
        """
        Percolate up the ith node.
        :param i: int, index of the heap list
        :return: No return
        """
        while (i - 1) // 2 >= 0:
            if self.heap[i] < self.heap[(i - 1) // 2]:
                self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2

    def insert(self, val):
        """
        Insert val to the heap.
        :param val: int
        :return: No return
        """
        self.heap.append(val)
        self.size += 1
        self._percolate_up(self.size - 1)

    def _min_child(self, i):
        """
        Find the min child of ith node
        :param i: int
        :return: No return
        """
        if i * 2 + 2 > self.size - 1:
            return i * 2 + 1
        else:
            if self.heap[i * 2 + 1] < self.heap[i * 2 + 2]:
                return i * 2 + 1
            else:
                return i * 2 + 2

    def _percolate_down(self, i):
        """
        Percolate down the ith node.
        :param i: int
        :return: No return
        """
        while (i * 2 + 1) < self.size:
            mc = self._min_child(i)
            if self.heap[i] > self.heap[mc]:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc

    def del_min(self):
        ret_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.size -= 1
        self.heap.pop()
        self._percolate_down(0)
        return ret_val

    def build_heap(self, lst):
        """
        Build a min heap with a given list.
        :param lst: list
        :return:
        """
        i = len(lst) // 2
        self.size = len(lst)
        self.heap = lst[:]
        while i >= 0:
            self._percolate_down(i)
            i -= 1


class Heap(object):
    def __init__(self):
        self.array = []

    def _sift_up(self, array, index):
        parent_idx = (index - 1) // 2
        if parent_idx < 0 or array[index] > array[parent_idx]:
            return
        array[index], array[parent_idx] = array[parent_idx], array[index]
        self._sift_up(array, parent_idx)

    def push(self, val):
        self.array.append(val)
        self._sift_up(self.array, len(self.array) - 1)

    def _sift_down1(self, array, index):
        left = index * 2 + 1
        right = index * 2 + 2
        small = index
        if left < len(array) and array[small] > array[left]:
            small = left
        if right < len(array) and array[small] > array[right]:
            small = right
        if small != index:
            array[small], array[index] = array[index], array[small]
            self._sift_down1(array, small)

    def _sift_down2(self, array, index):
        left = index * 2 + 1
        right = index * 2 + 2
        while left < len(array) or right < len(array):
            smaller = index
            if left < len(array) and array[smaller] > array[left]:
                smaller = left
            if right < len(array) and array[smaller] > array[right]:
                smaller = right
            if smaller == index:
                break
            array[index], array[smaller] = array[smaller], array[index]
            index = smaller
            left = index * 2 + 1
            right = index * 2 + 2

    def pop(self):
        res = self.array[0]
        self.array[0], self.array[-1] = self.array[-1], self.array[0]
        self.array.pop()
        self._sift_down2(self.array, 0)
        return res

    def build_heap(self, array):
        for i in range(len(array) // 2 - 1, -1, -1):
            self._sift_down2(array, i)


if __name__ == "__main__":
    a1 = [9, 6, 5, 2, 3]
    print("Original list:", a1)
    minHeap = BinaryMinHeap()
    minHeap.build_heap(a1)
    print("Newly created min heap:", minHeap.heap)
    print("Current size:", minHeap.size)

    minHeap.insert(1)
    print("Heap after inserting 1:", minHeap.heap)
    print("Current size:", minHeap.size)

    minHeap.del_min()
    print("Heap after deleting min:", minHeap.heap)
    print("Current size:", minHeap.size)
