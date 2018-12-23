class Solution:
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # A中可能有正有负数，所以不一定sun(A)最大
        length = len(A)
        # 输入规范审查
        if length == 0 or length > 50000 or K < 1 or K > 10**9:
            print('不符合输入格式要求')
            return
        for e in A:
            if e < -10**5 or e > 10**5:
                print('不符合输入格式要求')
                return
        min_len = length + 1
        for i in range(length):
                if A[i] <= 0:
                    continue
                for j in range(i+1, length+1):

                    if sum(A[i: j]) >= K:
                        print(i, j)
                        if j-i == 1:
                            return 1
                        min_len = min(min_len, j-i)
                        break
        return min_len if min_len < length + 1 else -1


if __name__ == '__main__':
    A = [2, -1, 2]

    # A = [3]
    K = 3
    sol = Solution()
    print(sol.shortestSubarray(A, K))