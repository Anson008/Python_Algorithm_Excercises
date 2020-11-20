class Solution(object):
    def dedup(self, array):
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
