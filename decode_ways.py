class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        else:
            s = list(s)
            for i, c in enumerate(s):
                if c == '0':
                    try:
                        if i == 0:
                            return 0
                        if s[i - 1] not in ['1', '2']:
                            return 0
                        else:
                            s[i - 1] = '#'
                            s[i] = '#'
                    except:
                        return 0
            count = 1
            stack = []
            m = 1
            for i, c in enumerate(s):

                if i + 1 < len(s) and c != '#' and s[i + 1] != '#':
                    if int(c) == 1:
                        count += 1
                        stack.append(i)
                    elif int(c) == 2 and int(s[i + 1]) < 7:
                        count += 1
                        stack.append(i)
                    else:
                        pass
            if len(stack) < 2:
                return count
            else:
                pre = stack[0]
                for index in stack:
                    if index - pre > 1:
                        m += 1
                        pre = index
            return count + 2 ** m - 1 - m


if __name__ == '__main__':
    sol = Solution()
    print(sol.numDecodings('1'))
