# encoding : utf-8
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if str == '':
            return 0
        re_value = 0
        try:
            if str[1:].isdigit():
                re_value = int(float(str))
            else:
                raise Exception
        except:
            sub_str = ''
            if str[0] in ['-', '+'] or (str[0] >= '0' and str[0] <= '9'):
                sub_str += str[0]
                for i in range(1, len(str)):
                    if str[i] >= '0' and str[i] <= '9':
                        sub_str += str[i]
                    else:
                        break
                if sub_str == '+' or sub_str == '-':
                    return 0
                else:
                    re_value = int(sub_str)
            else:
                re_value = 0

        '''越界处理'''
        if re_value > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif re_value < -2 ** 31:
            return -2 ** 31
        else:
            return re_value


if __name__ == '__main__':
    sol = Solution()
    print(sol.myAtoi('    -115579378e25'))