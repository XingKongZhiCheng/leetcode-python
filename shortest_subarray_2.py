from collections import deque
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
        if max(A) > K:
            return 1
        # p[i] = A[0] + A[i-1], P[0] = 0
        p = [0]
        for e in A:
            p.append(p[-1] + e)
        p_index_deque = deque()
        for x, px in enumerate(p):
            # 如果p[j]<=p[i](j>i),pop(i),(就是pop负数所在位置)
            while p_index_deque and px < p[p_index_deque[-1]]:
                p_index_deque.pop()
            # min(j-i)
            while p_index_deque and px - p[p_index_deque[0]] >= K:
                min_len = min(min_len, x-p_index_deque[0])
                # 越往后j-i越大，所以，若有符合条件的就可以删除
                # 如1,3符合， 后面还有符合的1,j也不肯能是最小的
                p_index_deque.popleft()
            # 添加p中元素的索引位置
            p_index_deque.append(x)
        return min_len if min_len < length + 1 else -1


if __name__ == '__main__':
    A = [2, -1, 2]

    # A = [3]
    K = 3
    sol = Solution()
    print(sol.shortestSubarray(A, K))