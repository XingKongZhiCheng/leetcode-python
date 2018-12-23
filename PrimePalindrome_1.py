
# n, 找出一个质数x，x>=n，并且（这个数左右对称）
# Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1
# Recall that a number is a palindrome if it reads the same from left to right as it does from right to left.

# For example, 12321 is a palindrome.
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
        if x < 2:
            return False
        if x < 10 and x in [2, 3, 5, 7]:
            return True
        i = 1
        # 若x不是质数， 必有一个p * q = x, p<math.sqrt(x)
        while i < int(math.sqrt(x)):
            i += 1
            if x % i == 0:
                return False
        return True

    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        if str(N) == str(N)[::-1] and self.is_prime(N):
            return N
        else:
            while True:
                N += 1
                if str(N) == str(N)[::-1] and self.is_prime(N):
                    return N
                if 10**7 < N < 10**8:
                    N = 10**8


if __name__ == '__main__':
    sol = Solution()
    print(sol.primePalindrome(14))