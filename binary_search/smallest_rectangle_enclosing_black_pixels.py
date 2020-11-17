class Solution(object):
    def minArea(self, image, x, y):
        """
        input: int[][] image, int x, int y
        return: int
        """
        # write your solution here
        num_rows = len(image)
        num_cols = len(image[0])
        if num_rows == 0 and num_cols == 0:
            return 0
        top = self.search_vertically(image, 0, x)
        bottom = self.search_vertically(image, x + 1, num_rows, False)
        left = self.search_horizontally(image, 0, y)
        right = self.search_horizontally(image, y + 1, num_cols, False)
        return (bottom - top) * (right - left)

    @staticmethod
    def search_vertically(image, left, right, top=True):
        while left < right:
            mid = (left + right) // 2
            if top:
                if 1 in image[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if 1 in image[mid]:
                    left = mid + 1
                else:
                    right = mid
        return left

    @staticmethod
    def search_horizontally(image, left, right, top=True):
        while left < right:
            mid = (left + right) // 2
            flag = False
            for p in image:
                if p[mid] == 1:
                    flag = True
                    break
            if top:
                if flag is True:
                    right = mid
                else:
                    left = mid + 1
            else:
                if flag is True:
                    left = mid + 1
                else:
                    right = mid
        return left
