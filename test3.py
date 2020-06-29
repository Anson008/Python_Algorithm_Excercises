class Solution(object):
  def decodeString(self, string):
    """
    input: string input
    return: string
    """
    # write your solution here
    multipliers = []
    string_stack = []
    letters = ''
    i = 0
    while i < len(string):
        if string[i].isdigit():
            multiplier = 0
            while string[i].isdigit():
                multiplier = multiplier * 10 + int(string[i])
                i += 1
        elif string[i].isalpha():
            letters += string[i]
            i += 1
        elif string[i] == '[':
            multipliers.append(multiplier)
            string_stack.append(letters)
            letters = ''
            i += 1
        else:
            multiplier = multipliers.pop()
            letters = string_stack.pop() + letters * int(multiplier)
            i += 1
    return letters


if __name__ == "__main__":
    s1 = '3[a]2[bc]'
    s2 = '2[abc]3[cd]ef'
    s3 = '34[a45[b]]'
    solu = Solution()
    res1 = solu.decodeString(s1)
    res2 = solu.decodeString(s2)
    res3 = solu.decodeString(s3)
    print(res1)
    print(res2)
    print(res3)