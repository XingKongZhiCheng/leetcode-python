# encoding : utf-8
# import numpy as np
# ------------------- problem ------------------
'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
(找在一条直线上最多的点数，返回其数目)
Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
'''


# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


class Solution:

    def get_max_points(self, arr, i, j):
        max_r = sum(arr[i][j:])
        max_d = sum(arr[:][j])
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
        size = 0
        for point in points:
            x = max(point)
            if x > size:
                size = x
        size += 1
        print(size)
        # arr = np.zeros(shape=(size, size))
        arr = [[0 for col in range(size)] for row in range(size)]
        print(arr)
        for point in points:
            # print(point)
            # arr[point[0]-1, point[1]-1] = 1

            # arr[point[0] - 1][point[1] - 1] = 1
            arr[point[0]][point[1]] = 1

        print(arr)

        max_ = 0
        # 扫描数组的边界点搜索
        for i in [0, size - 1]:
            for j in range(size):
                x = self.get_max_points(arr, i, j)
                if x > max_:
                    max_ = x
                if max_ == size-min([i, j]):
                    return max_

        for i in range(size):
            for j in [0, size - 1]:
                x = self.get_max_points(arr, i, j)
                if x > max_:
                    max_ = x
                if max_ == size-min([i, j]):
                    return max_
        return max_


if __name__ == '__main__':
    sol = Solution()
    # lst = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    # lst = [[1,1],[2,2],[3,3]]
    lst = [[1,1],[1,0]]
    # print('result:', sol.maxPoints(np.array(lst)))
    print('result:', sol.maxPoints(lst))