class Solution:
    @staticmethod
    def longest_sublist(arr):
        hash_set = set()
        longest = 0
        slow = fast = 0
        while fast < len(arr):
            while arr[fast] in hash_set:
                hash_set.remove(arr[slow])
                slow += 1
            hash_set.add(arr[fast])
            longest = max(longest, fast - slow + 1)
            fast += 1
        return longest


if __name__ == "__main__":
    arr1 = [1, 2, 3, 1, 4, 3]
    solu = Solution()
    res1 = solu.longest_sublist(arr1)
    print(res1)
