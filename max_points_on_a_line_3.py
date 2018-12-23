# encoding : utf-8
# Definition for a point.
import datetime
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    def get_max_points(self, arr, i, j):
        max_r = sum(arr[i][j:])
        # max_d = sum(arr[:][j])
        # 计算一列上的和
        max_d = 0
        for row in range(len(arr)):
            max_d += arr[row][j]
        max_r_d = arr[i][j]
        m = i
        n = j
        while m < len(arr)-1 and n < len(arr)-1:
            m += 1
            n += 1
            max_r_d += arr[m][n]

        max_l_d = arr[i][j]
        m = i
        n = j
        while m < len(arr)-1 and n > 0:
            m += 1
            n -= 1
            max_l_d += arr[m][n]

        return max([max_r, max_d, max_r_d, max_l_d])

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        # 确定数组的规模
        # size = np.max(points)  # 不能使用np
        max_size = 0
        min_size = 0
        for point in points:
            x = max(point.x, point.y)
            y = min(point.x, point.y)
            if x > max_size:
                max_size = x
            if y < min_size:
                min_size = y
        max_size += 1  # 没有size+1,则 loc-1
        if min_size < 0:
            max_size -= min_size
        # print(size)
        # arr = np.zeros(shape=(max_size, max_size))
        arr = [[0 for col in range(max_size)] for row in range(max_size)]
        print(arr)
        for point in points:
            # print(point)
            if min_size < 0:
                point.x -= min_size
                point.y -= min_size
            arr[point.x][point.y] += 1  # 两个相同的点，当做两个点
        print(arr)

        max_ = 0
        # 扫描数组的边界点搜索  # 不能只从边界开始搜索
        # 扫描所有点
        for i in range(max_size):
            for j in range(max_size):
                x = self.get_max_points(arr, i, j)
                if x > max_:
                    max_ = x
                # if max_ == max_size-min([i, j]):
                #     return max_
        return max_


if __name__ == '__main__':
    # 计算在一条线上的最多的点数
    sol = Solution()
    # 创建点
    p1 = Point(0, 0)
    # p1 = Point(1, 1)
    p2 = Point(1, 0)
    lst = [p1, p2]
    # print('result:', sol.maxPoints(np.array(lst)))
    start = datetime.datetime.now()
    print('result:', sol.maxPoints(lst))
    end = datetime.datetime.now()