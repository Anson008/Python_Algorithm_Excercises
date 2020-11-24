class Solution(object):
    @staticmethod
    def dedup1(array):
        """
        input: int[] array
        return: int[]
        """
        # write your solution here
        n = len(array)
        if n <= 1:
            return array
        j = 0
        for i in range(n - 1):
            if array[i] != array[i + 1]:
                array[j] = array[i]
                j += 1
        array[j] = array[n - 1]
        return array[:j+1]

    @staticmethod
    def dedup2(array):
        n = len(array)
        if n <= 1:
            return array
        i, j = 0, 0
        while i <= n - 1:
            count = 0
            while i < n - 1 and array[i] == array[i + 1]:
                count += 1
                if count <= 1:
                    array[j] = array[i]
                    j += 1
                i += 1
            array[j] = array[i]
            j += 1
            i += 1
        return array[:j]

    @staticmethod
    def dedup3(array):
        n = len(array)
        if n <= 1:
            return array
        i, j = 0, 0
        while i <= n - 1:
            count = 0
            while i < n - 1 and array[i] == array[i + 1]:
                count += 1
                i += 1
            if count == 0:
                array[j] = array[i]
                j += 1
            i += 1
        return array[:j]

    def dedup4(self, array):
        n = len(array)
        if n <= 1:
            return array
        i, j = 0, 1
        while j <= n - 1:
            if i >= 0 and array[j] == array[i]:
                while j <= n - 1 and array[j] == array[i]:
                    j += 1
                i -= 1
            else:
                array[i + 1] = array[j]
                j += 1
                i += 1
        return array[:i + 1]


if __name__ == "__main__":
    a1 = [1, 2, 2, 2, 3, 3, 3, 3]
    a2 = [1, 2, 3]
    a3 = [1, 2, 2, 3, 3, 3, 2, 2]
    solu = Solution()
    print(solu.dedup2(a1))
    print(solu.dedup2(a2))
    print(solu.dedup3(a1))
    print(solu.dedup3(a2))
    print(solu.dedup3(a3))




