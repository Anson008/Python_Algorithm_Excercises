class Solution:
    def bt_subsequence(self, arr, level, subsequence, subsequences):
        if level == len(arr):
            subsequences.append(subsequence[:])
            return
        subsequence.append(arr[level])
        self.bt_subsequence(arr, level + 1, subsequence, subsequences)
        subsequence.pop()
        while level + 1 < len(arr) and arr[level] == arr[level + 1]:
            level += 1
        self.bt_subsequence(arr, level + 1, subsequence, subsequences)

    def all_subsequences(self, arr):
        subsequence, subsequences = [], []
        self.bt_subsequence(arr, 0, subsequence, subsequences)
        return subsequences


if __name__ == "__main__":
    arr1 = ['a', 'b', 'b']
    solu = Solution()
    res1 = solu.all_subsequences(arr1)
    print(res1)
