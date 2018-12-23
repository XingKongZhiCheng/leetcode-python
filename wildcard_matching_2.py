import re
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 将p中多个连续的*转换为一个,并将p转换为re需要的形式
        temp = []
        for i in range(len(p)):
            if p[i] == '*' and p[i-1] == '*' and i > 0:
                continue
            elif p[i] == '*':
                temp.append('[a-z]*')
            elif p[i] == '?':
                temp.append('.')
            else:
                temp.append(p[i])
        p_trans = ''
        for e in temp:
            p_trans += e
        print('p:', p_trans)

        # # 将p转换为re需要的形式
        # p1 = []
        # for i in range(len(p)):
        #     if p[i] == '*':
        #         p1.append('[a-z]*')
        #     elif p[i] == '?':
        #         p1.append('.')
        #     else:
        #         p1.append(p[i])
        # p_trans = ''
        # for e in p1:
        #     p_trans += e
        # print('p_trans:', p_trans)
        try:
            span = re.search(p_trans, s).span()
            if span[0] == 0 and span[1] == len(s):
                return True
        except:
            return False
        return False


if __name__ == '__main__':
    sol = Solution()
    # s = "aa"
    # p = "*"

    # s = "adceb"
    # p = "*a*b"

    # s = "acdcb"
    # p = "a*c?b"

    # s = "aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba"
    # p = "*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*"
    #
    s = "aabbbaaaabbbabbabaaabaaabababbbbbaaababbbababaaaaaabbabaaaababbbababababbbbabaaaaabbabbabbbbbabbabaaaa"
    p = "b***bbb*b*bb***a*ba*b**aab*abb**aabb**a**baba*b*abbba"
    print(sol.isMatch(s, p))