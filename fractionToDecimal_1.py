'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"

'''
class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # numerator//denominator, numerator%denominator
        n, remainder = divmod(abs(numerator), abs(denominator))
        # 确定结果的 ‘+’， ‘-’
        sign = '-' if numerator * denominator < 0 else ''
        result = [sign + str(n), '.']  # 相除结果的整数部分 和 小数点
        if remainder == 0:
            return ''.join(result[:-1])
        stack = []
        # 如果remainder之前出现过，现在又出现，之后也会一直出现，（应为除数不会变）
        # 可能是一个字符重复出现，也肯能是多个字符循环出现
        # 不过只要小数部分重复出现两次 相同的字符，都可以停止操作，应为之后会循环出现之前的字符

        '''
        example:
        1    (2, 3) : remainder = 2
        2    (20, 3) : remainder = 2
        stack = [2] result['整数部分', '.', '6']
        
        1    (22, 100) : remainder = 22
        2    (220, 100) : remainder = 20
        2    (200, 100) : remainder = 0
        stack = [22, 20, 0] result['整数部分', '.', '2', '2']
        '''
        # 前面出现过，则退出
        is_cycle = 1  # 出现循环标志
        while remainder not in stack:  # 若remainder == 0,退出
            if remainder == 0:
                is_cycle = 0  # 并非出现循环而退出
                break
            # 如果remainder之前出现过，现在又出现，之后也会一直出现，（应为除数不会变）
            # 所以这里用remainder， 而不是用n， 所以需要一个额外的stack
            stack.append(remainder)
            # 每一次都是 余数 * 10 （//,%）得到新的整数和小数，相当于小数点右移
            n, remainder = divmod(remainder * 10, abs(denominator))
            result.append(str(n))  # 结果的小数部分

        if is_cycle == 1:
            # 出现重复remainder， 退出循环
            # 开始出现循环的起始位置
            loc = stack.index(remainder)  # （在小数部分中的索引）stack: 0--- result:2
            result.insert(2 + loc, '(')
            result.append(')')
        return ''.join(result)


if __name__ == '__main__':
    sol = Solution()
    print(sol.fractionToDecimal(1, 6))
    print(sol.fractionToDecimal(11, 100))