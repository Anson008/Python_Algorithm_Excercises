def bt_combination(results, comb, n, k):
    if len(comb) == k:
        results.append(comb[:])
        return
    for num in range((comb[-1] + 1) if comb else 1, n + 1):
        comb.append(num)
        bt_combination(results, comb, n, k)
        comb.pop()


def generate_combination(n, k):
    results, comb = [], []
    bt_combination(results, comb, n, k)
    return results


class Solution:
    def bt_combination(self, arr, level, comb, combs, k):
        if len(comb) == k:
            combs.append(comb[:])
            return
        if level == len(arr):
            return
        comb.append(arr[level])
        self.bt_combination(arr, level + 1, comb, combs, k)
        comb.pop()
        while level + 1 < len(arr) and arr[level] == arr[level + 1]:
            level += 1
        self.bt_combination(arr, level + 1, comb, combs, k)

    def all_combinations(self, arr, k):
        comb, combs = [], []
        self.bt_combination(arr, 0, comb, combs, k)
        return combs


if __name__ == "__main__":
    res = generate_combination(3, 2)
    print(res)

    solu = Solution()
    arr1 = ['a', 'b', 'c']
    arr2 = ['a', 'b', 'b']
    arr3 = [1, 2, 2, 2, 3]
    res1 = solu.all_combinations(arr1, 2)
    res2 = solu.all_combinations(arr2, 2)
    res3 = solu.all_combinations(arr3, 3)
    print(res1)
    print(res2)
    print(res3)
