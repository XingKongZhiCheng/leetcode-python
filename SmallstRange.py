'''
Given an array A of integers, for each integer A[i] we need to choose
either x = -K or x = K, and add x to A[i] (only once).

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.

'''
class Solution:
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        min_value, max_value = A[0], A[-1]
        '''
        1 分析， 当所有元素，同时 + k（或 - k），max-min不变
        2 要使 max-min变小， 肯定要在min+k, max-k范围内寻找
        3 将 A 排序，最小的极有可能是max(e2+k, A[-1]-k) - min(A[0]+k, e2-k ) (e1,e2相邻)， 或者 
        '''
        ans = max_value - min_value  #
        # 每一次， i+1之前的元素，都是+k，others -K
        for i in range(len(A)-1):
            ans = min(ans, max(A[i]+K, max_value-K)-min(min_value+K, A[i+1]-K))
        return ans


if __name__ == '__main__':
    sol = Solution()
    arr = [6, 4, 10]
    k = 5
    print(sol.smallestRangeII(arr, k))