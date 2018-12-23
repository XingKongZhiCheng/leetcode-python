class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 创建一个rows：len(s)+1， columns:len(p)+1的布尔值数组
        dp = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True
        # print('dp"\n', dp)
        # 从1开始，dp[i][j] <->
        for i in range(1, len(p)+1):  # p 对应columns
            if p[i-1] == '*':
                if i >= 1:
                    dp[0][i] = dp[0][i-1]
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]
        return dp[len(s)][len(p)]


if __name__ == '__main__':
    sol = Solution()
    # s = "aa"
    # p = "*"

    # s = "adceb"
    # p = "*a*b"

    s = "acdcb"
    p = "a*c?b"

    # s = "aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba"
    # p = "*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*"
    #
    # s = "aabbbaaaabbbabbabaaabaaabababbbbbaaababbbababaaaaaabbabaaaababbbababababbbbabaaaaabbabbabbbbbabbabaaaa"
    # p = "b***bbb*b*bb***a*ba*b**aab*abb**aabb**a**baba*b*abbba"
    print(sol.isMatch(s, p))


