from datetime import datetime


class Solution:
    '''
    leetcode 上面别人的算法
    '''

    def _findSubstring(self, l, r, n, k, t, s, req, ans):
        '''
        在字符串s中取substring长度的字符串，
        应为每一个word的长度相同，所以很容易将该substring换分成单词，
        统计每一个单词在substring中的词频，它应当与req相同
        :param l:
        :param r:
        :param n: 字符串s长度
        :param k: 一个单词的长度，题目要求每个单词具有相同的长度
        :param t: substring 的长度
        :param s: 字符串s
        :param req: 统计每一个单词在words中的词频的字典
        :param ans: 要返回的结果
        :return:
        '''
        curr = {}
        while r + k <= n:
            w = s[r:r + k]  #
            r += k
            # 如果该单词不在req，skip
            if w not in req:
                l = r
                curr.clear()
            else:
                curr[w] = curr[w] + 1 if w in curr else 1
                while curr[w] > req[w]:
                    curr[s[l:l + k]] -= 1
                    l += k
                if r - l == t:
                    ans.append(l)

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
        req = {}
        # 统计每一个单词在words中的词频
        for w in words:
            req[w] = req[w] + 1 if w in req else 1
        ans = []
        for i in range(min(k, n - t + 1)):
            self._findSubstring(i, i, n, k, t, s, req, ans)
        return ans


if __name__ == '__main__':
    start = datetime.now()
    s = "pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel"
    words = ["dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg","ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"]
    sol = Solution()
    print(sol.findSubstring(s, words))
    end = datetime.now()
    print('cost time:', end-start)
