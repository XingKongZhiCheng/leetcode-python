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


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # 第一种情况
        if endWord not in wordList:
            return []
        else:
            # All words have the same length.
            length = len(beginWord)
            # 存储所有不同的路径
            trans_path_words = []
            path_count = 0
            for word in wordList:
                # 与beginWord不相同的字符个数
                diff_begin_count = 0
                for i in range(length):
                    if word[i] != beginWord[i]:
                        diff_begin_count += 1
                if diff_begin_count == 1:
                    temp1 = [beginWord, word]
                    for path in search_path(word, endWord, wordList, temp1):
                        trans_path_words.append([])
                        trans_path_words[path_count] = path
                        path_count += 1
            # 获取最短路径：
            print('paths:', trans_path_words)
            min_len = len(trans_path_words[0])
            for path2 in trans_path_words:
                if len(path2) < min_len:
                    min_len = len(path2)
            shortest_paths = []
            for path3 in trans_path_words:
                if len(path3) == min_len:
                    print('path:', path3)
                    shortest_paths.append(path3)
            return shortest_paths


def search_path(start_word, end_word, word_list, trans_words):
        # All words have the same length.
        length = len(start_word)
        diff_start_count = 0

        sel_next_words = []
        for word in word_list:
            if word not in trans_words:
                for i in range(length):
                    if word[i] != start_word[i]:
                        diff_start_count += 1
                if diff_start_count == 1:
                    sel_next_words.append(word)
                diff_start_count = 0
        # 路径规划
        poss_words_path = []
        poss_count = 0
        if end_word in sel_next_words:
            trans_words.append(end_word)
            print('trans_words:', trans_words)
            return trans_words
        else:
            for word2 in sel_next_words:

                temp2 = trans_words
                temp2.append(word2)
                paths = search_path(word2, end_word, word_list, temp2)
                if paths == []:
                    continue
                if type(paths[0]) == list and len(paths) > 1:
                    for path in paths:
                        if end_word in path:
                            poss_words_path.append([])
                            poss_words_path[poss_count] = path
                            poss_count += 1
                        else:
                            search_path(path[-1], end_word, word_list, path)
                else:
                    if end_word in paths:
                        print('paths', paths)
                        return [paths]
                        # print('end in paths:', paths)
                        # poss_words_path.append(paths)
                        # poss_count += 1
                        # continue

                    else:
                        # print(paths)
                        search_path(paths[0][-1], end_word, word_list, paths[0])
        print('poss_words_path:', poss_words_path)
        return poss_words_path


if __name__ == '__main__':
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    # wordList = ["hot","dot","dog","lot","log"]
    sol.findLadders(beginWord, endWord, wordList)

