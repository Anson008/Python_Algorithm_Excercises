class _TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class Solution:
    def bst(self, arr, start, end):
        if start > end:
            return
        mid = (start + end) // 2  # or mid = (start + end + 1) // 2
        root = _TreeNode(arr[mid])
        root.left = self.bst(arr, start, mid - 1)
        root.right = self.bst(arr, mid + 1, end)
        return root

    def create_bst(self, arr):
        if not arr:
            return
        return self.bst(arr, 0, len(arr) - 1)

    def sorted_linked_list_to_bst(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return self.create_bst(arr)

