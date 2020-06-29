class SolutionGab:
    def bt_subset_duplicates(self, subsets, subset, current_stage, N, nums):
        if current_stage == len(nums):
            subsets.append(subset[:])
            return
        subset.append(nums[current_stage])
        self.bt_subset_duplicates(subsets, subset, current_stage + 1, N, nums)
        subset.pop()
        i = current_stage + 1
        while i < len(nums) and nums[current_stage] == nums[i]:
            i += 1
        self.bt_subset_duplicates(subsets, subset, i, N, nums)
        return

    def all_subsets_duplicates(self, nums):
        subsets, subset = [], []
        self.bt_subset_duplicates(subsets, subset, 0, len(nums), nums)
        return subsets


class Solution:
    def bt_subset(self, arr, level, subset, subsets):
        if level == len(arr):
            subsets.append(subset[:])
            return
        subset.append(arr[level])
        self.bt_subset(arr, level + 1, subset, subsets)
        subset.pop()
        while level + 1 < len(arr) and arr[level] == arr[level + 1]:
            level += 1
        self.bt_subset(arr, level + 1, subset, subsets)

    def all_subsets(self, arr):
        subsets, subset = [], []
        self.bt_subset(arr, 0, subset, subsets)
        return subsets


if __name__ == "__main__":
    solu = Solution()
    solu_gab = SolutionGab()
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 2]
    nums3 = ['a', 'b', 'a', 'b']

    res1 = solu.all_subsets(nums1)
    print(res1)

    res2 = solu.all_subsets(nums2)
    print(res2)

    res3 = solu.all_subsets(nums3)
    print(res3)

    res13 = solu_gab.all_subsets_duplicates(nums2)
    print(res13)

    res14 = solu_gab.all_subsets_duplicates(nums1)
    print(res14)
