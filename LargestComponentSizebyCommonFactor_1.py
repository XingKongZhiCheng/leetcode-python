class Solution:
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def is_have_common_factor(a, b):
            if min(a, b) < 2:
                return False
            for m in range(2, min(a, b) + 1):
                if (a % m == 0) and (b % m == 0):
                    return True
            return False

        # create adj array
        length = len(A)
        arr = [[0 for _ in range(length)] for __ in range(length)]

        # add edge
        for i in range(length):
            arr[i][i] = 1
            for j in range(i + 1, length):
                if is_have_common_factor(A[i], A[j]):
                    arr[i][j] = 1
                    arr[j][i] = 1
        # print('arr0:\n', arr)

        # 找出最大连通分量


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestComponentSize([65,35,43,76,15,11,81,22,55,92,31]))