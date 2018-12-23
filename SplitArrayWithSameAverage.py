
'''
Change the quesiton change to a N-sum problem:
To find if
1 element with sum = 1 * avg or
2 elements with sum = 2 * avg or
i elements with sum = i * avg

The size of smaller list between B and C will be less than N/2+1, so 0 < i < N/2+1

sum * i/length : 保证结果为整数
'''
class Solution:
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        def find_sub_arr(count, target, start):
            if count == 0:
                print('target == 0:', target == 0)
                return target == 0
            if count + start > n:
                return False
            return find_sub_arr(count - 1, target - A[start], start + 1) or find_sub_arr(count, target, start + 1)

        if len(A) < 2:
            return False
        elif len(A) == 2:
            if A[0] == A[1]:
                return True
            else:
                return False
        else:
            s, n = sum(A), len(A)
            if s / n in A:
                return True
            for i in range(2, n // 2 + 1):
                # 用s*i/n保证结果是整数
                if find_sub_arr(i, s * i / n, 0):  # True or False
                    return True

        return False


if __name__ == '__main__':
    sol = Solution()
    arr = [0, 13, 13, 7, 5, 0, 10, 19, 5]
    print(sol.splitArraySameAverage(arr))