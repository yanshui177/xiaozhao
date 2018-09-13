#-*- coding:utf-8 -*-
"""
无重复最大长度
"""
from math import ceil


def fuc(string):
    n = 0
    temp = []
    temp_len = []
    for i in range(len(string)):
        for i in range(i, len(string)):
            if string[i] not in temp:
                temp.append(string[i])
            else:
                break
        temp_len.append(len(temp))
    return max(temp_len)


if __name__ == '__main__':
    string = raw_input().strip()
    res = fuc(string)
    print res