# encoding : utf-8
import sys
'''
Given two words (beginWord and endWord), and a dictionary's word list,
find all shortest transformation sequence(s) from beginWord to endWord, such that:
（将beginword 转化为 endword ，每次都从列表中选取最短的wordlist）
Only one letter can be changed at a time(每次只能改变一个字符)
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
(如果没有转换词序列返回一个[])
All words have the same length.(所有词长度相同)
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.（没有重复的字）
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''
sys.setrecursionlimit(100000)  # 例如这里设置为一万
import gc


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList[:]:
            print('the end_word not in word_list')
            return []
        else:
            trans_word_list = []
            count = 0
            for word in wordList:
                # word_list = list(word)
                dif_count = 0
                for i in range(len(word)):
                    if beginWord[i] != word[i]:
                        dif_count += 1
                if dif_count == 1:
                    trans_word_list.append([])
                    trans_word_list[count].append(beginWord)
                    trans_word_list[count].append(word)
                    trans_word_list[count] = self.search(word, endWord, wordList, trans_word_list[count])
                    # print(trans_word_list[count])
                    count += 1
        min_len = len(wordList) + 1
        loc_in = 0
        i = 0
        for trans in trans_word_list:

            if len(trans) < min_len:
                min_len = len(trans)
                loc_in = i
            i += 1
        print('trans_word_list:\n', trans_word_list)
        print('shortest words：')
        for trans_ in trans_word_list:
            if len(trans_) == len(trans_word_list[loc_in]):
                print(trans)
        return trans_word_list

    def search(self, begin_word, end_word, word_list, trans_list):
        sel_words = []
        # 挑选只相差一个字符的单词
        for word1 in word_list:
            if word1 not in trans_list:
                dif_count = 0
                for i in range(len(word1)):
                    if begin_word[i] != word1[i]:
                        dif_count += 1
                if dif_count == 1:

                    if word1 == end_word:
                        trans_list.append(word1)
                        return trans_list
                    else:
                        sel_words.append(word1)
        # 挑选最相似的的单词

        ret_trans_list = []
        selected_words = self.most_similar(end_word, sel_words)
        for sel_word in selected_words:
            # 得到最短字序列后会返回
            trans_list.append(sel_word)
            temp = trans_list  # trans_list 为什么成了嵌套中的全局变量
            self.search(sel_word, end_word, word_list, temp)
            if end_word == trans_list[-1]:
                ret_trans_list.append(trans_list)
                # return trans_list
            trans_list = temp
            # gc.collect()
        # return trans_list
        return ret_trans_list

    # 找最匹配的word（即相似度最高的）
    def most_similar(self, x, word_list):
        max_ = 0
        sel_index = []

        for word in word_list:
            count = 0
            for i in range(len(x)):
                if x[i] == word[i]:
                    count += 1
            if count == max_:
                sel_index.append(word)
            if count > max_:
                sel_index.clear()
                sel_index.append(word)
                max_ = count
        return sel_index


if __name__ == '__main__':
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    # wordList = ["hot","dot","dog","lot","log"]
    sol.findLadders(beginWord, endWord, wordList)





