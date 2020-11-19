class Solution1(object):
    @staticmethod
    def move_zero(array):
        """
        input: int[] array
        return: int[]
        """
        # write your solution here
        if len(array) == 0:
            return array
        i, j = 0, len(array) - 1
        while j >= i:
            if array[j] != 0:
                break
            j -= 1
        while i < j:
            if array[i] == 0:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1
                while j >= i:
                    if array[j] != 0:
                        break
                    j -= 1
            else:
                i += 1
        return array


class Solution2(object):
    @staticmethod
    def move_zero(array):
        """
        input: int[] array
        return: int[]
        """
        # write your solution here
        if len(array) == 0:
            return array
        zero_stack = []
        nonzero_stack = []
        for j in range(len(array) - 1, -1, -1):
            if array[j] == 0:
                zero_stack.append(array.pop())
            else:
                nonzero_stack.append(array.pop())
        while len(nonzero_stack) > 0:
            array.append(nonzero_stack.pop())
        return array + zero_stack



