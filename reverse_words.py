# encoding : utf-8
'''
Given an input string, reverse the string word by word.

Example:

Input: "the sky is blue",
Output: "blue is sky the".
Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
Follow up: For C programmers, try to solve it in-place in O(1) space.
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        s_words = s.split(' ')
        # print(s_words)
        if len(s_words) == 0:
            return ''
        s = ''
        for word in s_words[::-1]:
            if word != '':
                s += word + ' '

        return s.strip()


if __name__ == '__main__':
    s_in = "the sky is   blue"
    sol = Solution()
    print(sol.reverseWords(s_in))