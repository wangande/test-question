#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ListNode(object):
    """链表结构"""
    def __init__(self, val):
        self.val = val
        self.next = None


def insert_node(single_list, val):
    """
    节点插入，使用尾插法
    :param single_list: 链表
    :param val: 数据
    :return:single_list
    """
    if not single_list:
        # 初始时候，节点为空，直接将生成的节点赋给single_list
        single_list = ListNode(val)
        single_list.next = None
    else:
        new_node = ListNode(val)
        p = single_list     # 保证头指针位置不变
        while p.next:
            p = p.next
        p.next = new_node

    return single_list


def list_reversed(single_list):
    """
    递归,实现反向
    :param single_list: 链表
    :return:
    """

    if (not single_list) or (not single_list.next):
        return single_list

    reversed_list = list_reversed(single_list.next)
    single_list.next.next = single_list
    single_list.next = None

    return reversed_list


def show_list(single_list):
    """
    显示list
    :param single_list: 链表
    :return:
    """
    tmp_node = single_list    # 防止head位置变化
    node_data = []
    while tmp_node:
        node_data.append(tmp_node.val)
        tmp_node = tmp_node.next
    print node_data

if __name__ == "__main__":
    list_head = None
    for data in range(0, 10):
        list_head = insert_node(list_head, data)

    show_list(list_head)
    reversed_list = list_reversed(list_head)
    show_list(reversed_list)

