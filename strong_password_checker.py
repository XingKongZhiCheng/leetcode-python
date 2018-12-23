# encoding : utf-8
'''
A password is considered strong if below conditions are all met:
(密码是强壮的条件)
1 （6-20个字符）
It has at least 6 characters and at most 20 characters.

2（至少包含一个小写字母和一个大写字母，和一个数字）
It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.

3（一个字母不能连续重复三次以上）
It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..."
is strong, assuming other conditions are met).

# 如果输入的字符串不够强壮，返回最小的变化使其强壮，反之，返回0（强壮）
Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change
required to make s a strong password. If s is already strong, return 0.
Insertion, deletion or replace of any one character are all considered as one change.
'''


class Solution:
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """

        # condition 2 （至少包含一个小写字母和一个大写字母，和一个数字）
        def contain_detect(s1):
            count1 = 0
            count2 = 0
            count3 = 0
            for e in s1:
                if e>='a' and e<='z':
                    count1 = 1
                if e>='A' and e<='Z':
                    count2 = 1
                if e>='0' and e<='9':
                    count3 = 1
            return count1 + count2 + count3

        # condition 3（一个字母不能连续重复三次即以上）
        def re_char_detect(s2):
            re_ch_save = []
            # 单个字符重复
            length = len(s2)
            loc = 0

            while True:
                try:
                    e = s2[loc]
                    if s2[loc:].count(e) >= 3 and 3*e in s2[loc:]:
                        start = s2[loc:].index(3*e) + loc

                        for i in range(start, length):
                            if s2[i] != e:
                                end = i-1
                                break
                            if i == length - 1:
                                end = i
                        # print('start:', start)
                        # print('end', end)
                        re_ch_save.append(end-start+1)
                        loc = end+1
                    else:
                        loc += 1
                except:
                    break

            # print('re_ch:', re_ch_save)
            if len(re_ch_save) > 0:
                # print('re_ch', re_ch_save)
                return re_ch_save
            return [0]

        # condition 1 （6-20个字符）
        length = len(s)
        insert = 0
        delete = 0
        replace2 = 0
        replace1 = 0
        if length < 6:
            # print('字符串长度不符合要求，请重新输入')
            insert = 6-length
            print('需要插入%d个字符' % insert)
            # return insert + abs(replace2 - replace1)
            # return -1
        if length > 20:
            delete = length - 20
            print('需要删除%d个字符' % delete)
        # condition 2 （至少包含一个小写字母和一个大写字母，和一个数字）
        # contain_kinds = contain_detect(s)
        if contain_detect(s) < 3:
            replace1 = 3-contain_detect(s)
            print('至少包含一个小写字母和一个大写字母，和一个数字,缺少%d种字符' % replace1)
            # return insert + abs(replace2 - replace1)
        # condition 3（一个字母不能连续重复三次以上）
        lst = re_char_detect(s)
        if True:
            # print('一个字母不能连续重复三次以上,')
            if lst[0] > 1:
                for ele in lst:
                    replace2 += ele - 2
            print('需要删除或者替换%d个字符' % replace2)
        print('s:', s)
        print('字符串长度', length)
        print('re_ch:', lst)
        if delete == 0 and insert > 0:
            if insert >= max(replace2, replace1):
                return insert
            replace = 0
            for ele in lst:
                # insert replace(1包含了必须的insert,2少于必须的insert)
                replace += ele // 3 + ele % 2
            return insert + max(max(replace-insert, 0), max(replace1-insert, 0))

        if delete == 0 and insert == 0:
            if lst[0] > 1:
                # print('一个字母不能连续重复三次以上,'
                replace = 0
                for ele in re_char_detect(s):
                    # 例如5个连续的字符，只需替换第三个字符
                    replace += ele//3
                # 必须确保包含三种字符
                replace = max(replace, replace1)
                # 最终的的replace次数>=replace1
                return max(min(replace, replace2), replace1)
            else:
                # replace2==0，insert==0
                return replace1

        if delete > 0:
            replace = 0
            if lst[0] > 1 and replace2 > replace1:
                if delete >= replace2:
                    return delete
                # print('一个字母不能连续重复三次以上,')
                del_count = 0
                # lst.sort()
                # 按删除后代价最小排序，比如3-1，就是最优的删除操作l
                lst_del_count = [e % 3 for e in lst]
                max_ = max(lst_del_count) + 1
                lst_del_index = []
                for i in range(len(lst)):
                    index = lst_del_count.index(min(lst_del_count))
                    lst_del_index.append(index)
                    lst_del_count[index] = max_
                print('删除操作优先顺序：', lst_del_index)
                # 记录ele>5的重复项个数
                ele_5_count = 0
                for i in lst_del_index:
                    ele = lst[i]
                    if ele >= 5:
                        ele_5_count += 1
                    flag = 0
                    if del_count < delete and ele//3 > (ele-1)//3:
                        ele -= 1
                        del_count += 1
                        flag = 1
                    if delete-del_count > 1 and ele//3 > (ele-2)//3 and flag == 0:
                        ele -= 2
                        del_count += 2
                    replace += ele//3
                # 所有重复项都经历了删除操作后，删除操作还有剩余，这个时候
                # 所有经处理的重复项一定是（e%3==2这种情况）
                min_sub = min(ele_5_count, (delete-del_count)//3)
                # 必须确保包含三种字符
                replace = max(replace-min_sub, replace1)
                return min(replace+delete, replace2)
            if replace2 <= replace1:
                return delete+replace1
            # if replace2 > delete:
            '''
            replace2 : 是重复的，完全可以用delete
            replace1的操作，必须要有，但可以包含在replace2中
            replace2特别大，可以插入
            '''
            #     return replace2
            # else:
            #     return delete + replace1
        if replace2 + replace1 + insert + delete == 0:
            return 0


if __name__ == '__main__':
    sol = Solution()
    # print(sol.strongPasswordChecker('Ac111123'))
    print(sol.strongPasswordChecker('aaa111'))
    print(sol.strongPasswordChecker("ABABABABABABABABABAB1"))
    print(sol.strongPasswordChecker("aaaaaaaaaaaaaaaaaaaaa"))
    print(sol.strongPasswordChecker('...'))
    print(sol.strongPasswordChecker('.....'))
    print(sol.strongPasswordChecker('aaaaa'))
    print(sol.strongPasswordChecker("qqq123qqq"))
    print(sol.strongPasswordChecker("..................!!!"))
    print(sol.strongPasswordChecker("aaaabbaaabbaaa123456A"))
    print(sol.strongPasswordChecker("aaaaaaaAAAAAA6666bbbbaaaaaaABBC"))
    print(sol.strongPasswordChecker(""))