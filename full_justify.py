# encoding : utf-8
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import


class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        length = len(words)
        if length == 1:
            return [words[0] + (maxWidth - len(words[0]))*' '] if maxWidth > len(words[0]) else words
        else:
            count = 0
            out = []
            start = 0
            for i in range(length):
                if start < i and count == 0:
                    count += len(words[start]) + 1
                count += len(words[i]) + 1
                if i == length-1 and count-1 <= maxWidth:
                    line = ''
                    for y in range(start, i+1):
                        if y == length - 1:
                            line += words[y] + (maxWidth-count+1) * ' '
                        else:
                            line += words[y] + ' '
                    out.append(line)
                elif count-1 > maxWidth:
                    line = ''
                    count -= len(words[i]) + 1

                    # 只有1个word
                    if i - start == 1:
                        line = words[start] + (maxWidth-count+1) * ' '
                        out.append(line)
                        if i == length - 1:
                            out.append(words[i] + (maxWidth - len(words[i])) * ' ')
                    else:
                        nor_space = (maxWidth - count+1) // (i - start - 1) + 1
                        more_space = (maxWidth-count+1) % (i-start-1)
                        for x in range(start, i):
                            if x == i-1:
                                line += words[x]
                            else:
                                if more_space > 0:
                                    line += words[x] + (nor_space+1) * ' '
                                    more_space -= 1
                                else:
                                    line += words[x] + nor_space * ' '
                        out.append(line)
                        if i == length - 1:
                            out.append(words[i] + (maxWidth - len(words[i])) * ' ')
                            # return out
                    count = 0
                    start = i
                    print('line:', line)
            return out


if __name__ == '__main__':
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    # words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    max_width = 16
    sol = Solution()
    print(sol.fullJustify(words, max_width))