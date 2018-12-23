class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        In [61]: True*3  # True 相当于 1
        Out[61]: 3

        In [62]: False * 3  # False 相当于 0
        Out[62]: 0
        '''
        # pre_char : 上一个 digit
        # cur_char ： 当前的 digit
        # pre_dw: tells the previous number of ways of decode
        # cur_dw : tells the current number of ways of decode
        if s == '':
            return 0
        else:
            pre_dw, cur_dw, pre_char = 0, 1, ''
            for d in s:
                '''
                a=1,b=2
                In [65]: a,b=b,a+b

                In [66]: a
                Out[66]: 2
                
                In [67]: b
                Out[67]: 3
                '''
                # 先执行 pre_dw = cur_dw 却不会影响接下来的计算
                pre_dw, cur_dw, pre_char = cur_dw, cur_dw * (d > '0') + (9 < int(pre_char+d) < 27) * pre_dw, d
        return cur_dw


if __name__ == '__main__':
    sol = Solution()
    '''
    p=0, c=1
    p = c, c = c * (d > '0') + p * (9 < int(pre_char+d) < 27)
    digit 1 : p:1, c=1 + 0*0 = 1
    digit 2 : p:1, c=1 + 1*1 = 2
    digit 1 : p:2, c=2 + 1*1 = 3
    digit 2 : p:3, c=3 + 1*2 = 5
    '''
    print(sol.numDecodings('1212'))