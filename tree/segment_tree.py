class SegmentTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = 0
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self, array):
        self.array = array
        self.root = self._build_segment_tree(array, 0, len(array) - 1)

    def update(self, index, value):
        diff = value - self.array[index]
        self.array[index] = value
        curr = self.root
        while curr is not None:
            curr.sum += diff
            mid = curr.start + (curr.end - curr.start) // 2
            if index <= mid:
                curr = curr.left
            else:
                curr = curr.right

    def sum(self, start, end):
        return self._get_sum_from_tree(self.root, start, end)

    def _build_segment_tree(self, array, start, end):
        if start > end:
            return None
        curr = SegmentTreeNode(start, end)
        if start == end:
            curr.sum = array[start]
            return curr
        mid = start + (end - start) // 2
        curr.left = self._build_segment_tree(array, start, mid)
        curr.right = self._build_segment_tree(array, mid + 1, end)
        if curr.left is not None:
            curr.sum += curr.left.sum
        if curr.right is not None:
            curr.sum += curr.right.sum
        return curr

    def _get_sum_from_tree(self, curr, start, end):
        if curr is None or curr.start > end or curr.end < start:
            return 0
        if curr.start >= start and curr.end <= end:
            return curr.sum
        return self._get_sum_from_tree(curr.left, start, end) + self._get_sum_from_tree(curr.right, start, end)


if __name__ == "__main__":
    s_tree = SegmentTree([1, 2, 3, 4, 5])
    print(s_tree.sum(1, 2))
    s_tree.update(1, 3)
    print(s_tree.sum(1, 2))
