class Solution(object):
    def convertToHex(self, n):
        res = []
        while n > 0:
            res.append(n % 16)
            n //= 16
        return res[::-1]

    def toHexspeak(self, num):
        x = self.convertToHex(int(num))
        ans = ""
        d = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F",0:"O",1:"I"}
        for i in x:
            if i in d:
                ans += d[i]
            else:
                return "ERROR"
        return ans