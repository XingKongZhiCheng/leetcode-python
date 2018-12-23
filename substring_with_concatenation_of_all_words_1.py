from datetime import datetime


class Solution:
    '''
    leetcode 上面别人的算法
    '''

    def _findSubstring(self, start, k, t, s, req, ans):
        '''
        在字符串s中取substring长度的字符串，
        应为每一个word的长度相同，所以很容易将该substring换分成单词，
        统计每一个单词在substring中的词频，它应当与req相同
        :param start: 其实搜索位置
        :param n: 字符串s长度
        :param k: 一个单词的长度，题目要求每个单词具有相同的长度
        :param t: substring 的长度
        :param s: 字符串s
        :param req: 统计每一个单词在words中的词频的字典
        :param ans: 要返回的结果
        :return:
        '''
        curr = {}
        count = 0  # words 计数
        l = start
        while count < t//k:
            word = s[l:l+k]
            if word in req.keys():
                curr[word] = curr[word] + 1 if word in curr.keys() else 1
            else:
                break
            l += k
            count += 1
        # print('start:', start)
        # print('ans:', ans)
        # print('curr:', curr)
        # print('req:', req)
        if curr == req:
            ans.append(start)
        return

    def findSubstring(self, s, words):
        # 如果
        if s == '' or words == []:
            return []
        # 字符串s长度
        n = len(s)
        # 一个单词的长度，题目要求每个单词具有相同的长度
        k = len(words[0])
        # substring 的长度
        t = len(words) * k
        if sum([len(word) for word in words]) % k != 0:
            return []
        req = {}
        # 统计每一个单词在words中的词频
        for w in words:
            req[w] = req[w] + 1 if w in req else 1
        ans = []
        # 有n - t + 1个Substring
        for i in range(n - t + 1):
            self._findSubstring(i, k, t, s, req, ans)
        return ans


if __name__ == '__main__':
    start = datetime.now()
    s = "barfoofoobarthefoobarman"
    words = ["bar", "foo", "the"]
    sol = Solution()
    print(sol.findSubstring(s, words))
    end = datetime.now()
    print('cost time:', end - start)
