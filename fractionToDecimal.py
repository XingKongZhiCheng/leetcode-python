from __future__ import print_function
from __future__ import division
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        s = str(numerator / denominator)
        if s.split('.')[1] == '0':
            s = s.split('.')[0]
        result = s[0]
        # 单个字符重复的情况
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                continue
            elif i + 1 < len(s) and s[i] == s[i + 1]:
                result += '(' + s[i] + ')'  # 保证它是相同字符中的第一个字符
            else:
                result += s[i]
        # 多个字符重复的情况
        return result

    def check_repeating(self, s):
        s_list = list(s)
        ch_repeat_index = []
        for i in range(len(s)):
            if s.count(s[i]) > 1:
                while True:
                    try:
                        ch_repeat_index.append(s_list.index(s[i]))
                        s_list[i] = '-'  # 变相删除，但不改变元素在源字符串中的索引位置
                    except:
                        break
                for start in range(len(ch_repeat_index)):
                    for end in range(1, len(ch_repeat_index)):
                        # 有待解决
                        pass

        return


if __name__ == '__main__':
    sol = Solution()
    print(sol.fractionToDecimal(2, 2))