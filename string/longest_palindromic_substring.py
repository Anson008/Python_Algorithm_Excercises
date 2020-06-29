class Solution:
    def longest_palindromic_substring(self, string):
        start = 0
        end = 0
        for i in range(len(string)):
            len1 = self.expand_around_center(string, i, i)
            len2 = self.expand_around_center(string, i, i + 1)
            longest = max(len1, len2)
            if longest > end - start + 1:
                start = i - (longest - 1) // 2
                end = i + longest // 2
        return string[start:end+1]

    @staticmethod
    def expand_around_center(string, left, right):
        while left >=0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        return right - left - 1


if __name__ == "__main__":
    str1 = 'abcbcbdefg'
    solu = Solution()
    res1 = solu.longest_palindromic_substring(str1)
    print(res1)