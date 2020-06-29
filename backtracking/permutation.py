def bt(answers, permutation, N, nums):
    if len(permutation) == N:
        answers.append(permutation[:])
        return
    for num in nums:
        if num not in permutation:
            permutation.append(num)
            bt(answers, permutation, N, nums)
            permutation.pop()
    return


def permute(nums):
    answers, permutation = [], []
    bt(answers, permutation, len(nums), nums)
    return answers


def bt_duplicates(answers, permutation, N, nums):
    if len(permutation) == N:
        answers.append(permutation[:])
        return
    used = set()
    for num in nums:
        if (num not in permutation or permutation.count(num) < nums.count(num)) and num not in used:
            used.add(num)
            permutation.append(num)
            bt_duplicates(answers, permutation, N, nums)
            permutation.pop()
    return


def permute_duplicates(nums):
    answers, permutation = [], []
    bt_duplicates(answers, permutation, len(nums), nums)
    return answers


class Solution:
    def bt_permutation(self, arr, level, answers):
        if level == len(arr):
            answers.append(arr[:])
            return
        used = set()
        for i in range(level, len(arr)):
            if arr[i] not in used:
                used.add(arr[i])
                arr[level], arr[i] = arr[i], arr[level]
                self.bt_permutation(arr, level + 1, answers)
                arr[level], arr[i] = arr[i], arr[level]

    def all_permutations(self, arr):
        answers = []
        self.bt_permutation(arr, 0, answers)
        return answers


if __name__ == "__main__":
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 2]
    res1 = permute(nums1)
    res2 = permute_duplicates(nums2)
    print(res1)
    print(res2)

    solu = Solution()
    res11 = solu.all_permutations(nums1)
    res12 = solu.all_permutations(nums2)
    print(res11)
    print(res12)
