#!/usr/bin/env python
# -*- coding: utf-8 -*-


class SubStringSearchKmp(object):
    """
    根据kmp实现的字符串查找算法，时间复杂度o(m+n)
    """

    def generate_next_list(self, sub_str):
        """
        生成next列表
        :param sub_str: 子字符串
        :return:
        """
        next_list = list()
        next_list.append(-1)    # 将-1添加到list中

        i = 0
        j = -1

        # 注意：这里比较的对象是ss的长度减去1
        # 如果是 while( i < lenOfSs) 会导致NEXT的长度比实际长度多1
        # 因为在一开始时已经将-1放入了list_next中，作为第一个字符的跳转值
        while i < len(sub_str) - 1:
            if j == (-1) or sub_str[i] == sub_str[j]:         # 如果满足条件
                print (i, j, sub_str[i], sub_str[j])
                i += 1
                j += 1
                next_list.append(j)
            else:   # 如果不满足字符相等的条件，执行该语句，而不是从0开始寻找最长相等的前缀与后缀的长度！！！简化计算
                j = next_list[j]
        return next_list

    def sub_string_match(self, sub_str, org_string):
        """
        字符串查找，若存在子字符串，返回匹配段的起点下标，否则返回-1
        :param sub_str: 子字符串
        :param org_string: 原始字符串
        :return: sub_string，在 org_string里面起点下标
        """

        sub_str_len = len(sub_str)                         # 计算子字符串的长度
        next_list = self.generate_next_list(sub_str)       # 构造next跳转表

        org_string_index = 0   # 指向主串 main_ss
        sub_string_index = 0   # 指向模式串 ss

        while (sub_string_index < sub_str_len) and (org_string_index < len(org_string)):

            if org_string[org_string_index] == sub_str[sub_string_index]:
                sub_string_index += 1
                org_string_index += 1

            elif org_string_index == 0:    # 如果第一个模式串的字符就不匹配，则移动指向主串的指针
                org_string_index += 1

            else:                          # 否则将指向模式串的指针移动至 list_next[sub_string_index]处
                sub_string_index = next_list[sub_string_index]

        if sub_string_index == sub_str_len:  # 如果完成匹配时， sub_str_len指向模式串的串尾，则匹配成功
            return org_string_index - sub_str_len
        else:
            return -1

if __name__ == "__main__":
    mp = SubStringSearchKmp()
    r = mp.sub_string_match("abce", "aabcabcebafabcabceabcaefabcacdabcababce")
    print r


