import heapq


class Solution:
    @staticmethod
    def oscillating_string(string):
        if string == '':
            return ''
        letters = list(string)
        stack = []
        heapq.heapify(letters)
        res = [heapq.heappop(letters)]
        while len(letters) > 0:
            if ord(letters[0]) > ord(res[-1]):
                res.append(heapq.heappop(letters))
            else:
                stack.append(heapq.heappop(letters))
        while len(stack) > 0:
            res.append(stack.pop())
        return ''.join(res)


if __name__ == "__main__":
    s1 = 'ababxyz'
    print(s1)
    solu = Solution()
    print(solu.oscillating_string(s1))
