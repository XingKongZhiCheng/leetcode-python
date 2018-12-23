
# n, 找出一个数x，x>=n
# Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1.

import math
class Solution(object):
    # 判断一个数是不是质数（除了1和它自身外，不能被其他自然数整除）
    '''
    我们继续分析，其实质数还有一个特点，就是它总是等于 6x-1 或者 6x+1，其中 x 是大于等于1的自然数。

    如何论证这个结论呢，其实不难。首先 6x 肯定不是质数，因为它能被 6 整除；
其次 6x+2 肯定也不是质数，因为它还能被2整除；依次类推，6x+3 肯定能被 3 整除；
6x+4 肯定能被 2 整除。那么，就只有 6x+1 和 6x+5 (即等同于6x-1) 可能是质数了。
所以循环的步长可以设为 6，然后每次只判断 6 两侧的数即可。


    '''
    def is_prime(self, x):
        if x < 10 and x in [2, 3, 5, 7]:
            return True
        if x % 6 ==1 or (x%6==5 and (x//6)%5!=0):
            return True
        return False

    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 2
        result = 0
        while True:
            i = 1
            N = N - N % 6 + 1
            lr_same = list(str(N))
            print(N)
            if lr_same == lr_same[::-1]:
                if self.is_prime(N):
                    return N
                elif N-2 > 0 and list(str(N-2)) == list(str(N-2))[::-1] and self.is_prime(N-2):
                    return N-2
                elif N < 10**8:
                    pass
                else:
                    return -1

            N += 6  # (6x+1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.primePalindrome(14))