
# n, 找出一个数x，x>=n
# Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1.
import math

class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 2
        while True:
            i = 1
            lr_same = list(str(N))
            # print(N)
            if lr_same == lr_same[::-1]:
                # 判断a number is prime
                # 假如n是合数，必然存在非1的两个约数p1和p2，其中p1<=sqrt(n)，p2>=sqrt(n)
                # while i <= N//2:  # 1 // 2 == 0
                while i <= int(math.sqrt(N)):
                    i += 1
                    if N % i == 0:
                        break
                # if i == N//2+1:
                if i == int(math.sqrt(N)) + 1:
                    return N
                elif N < 10**8:
                    pass
                else:
                    return -1
            N += 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.primePalindrome(12))