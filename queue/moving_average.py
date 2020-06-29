from collections import deque


class MovingAverage(object):
    def __init__(self, size):
        self.__window, self.__sum, self.size = deque(), 0, size

    def next(self, val):
        """

        :param val: int
        :return: float
        """
        if len(self.__window) == self.size:
            self.__sum -= self.__window.popleft()
        self.__window.append(val)
        self.__sum += val
        return self.__sum * 1. / len(self.__window)


if __name__ == "__main__":
    a1 = [3, 5, 2, 5, 9, -1, -8, 18, 2]
    moving_avg = MovingAverage(3)
    r1 = moving_avg.next(3)
    r2 = moving_avg.next(5)
    r3 = moving_avg.next(2)
    r4 = moving_avg.next(-1)
    print("{:.2f}, {:.2f}, {:.2f}, {:.2f}".format(r1, r2, r3, r4))
