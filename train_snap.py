#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
小易觉得高数课太无聊了，决定睡觉。不过他对课上的一些内容挺感兴趣，所以希望你在老师讲到有趣的部分的时候叫醒他一下。你知
道了小易对一堂课每分钟知识点的感兴趣程度，并以分数量化，以及他在这堂课上每分钟是否会睡着，你可以叫醒他一次，这会使得他
在接下来的k分钟内保持清醒。你需要选择一种方案最大化小易这堂课听到的知识点分值。
输入描述:
第一行 n, k (1 <= n, k <= 105) ，表示这堂课持续多少分钟，以及叫醒小易一次使他能够保持清醒的时间。
第二行 n 个数，a1, a2, ... , an(1 <= ai <= 104) 表示小易对每分钟知识点的感兴趣评分。
第三行 n 个数，t1, t2, ... , tn 表示每分钟小易是否清醒, 1表示清醒。

输出描述:
小易这堂课听到的知识点的最大兴趣值。
输入例子1:
6 3
1 3 5 2 5 4
1 1 0 1 0 0

输出例子1:
16
"""
import sys


def fuc(n, k, A, T):
    score = 0
    for i in range(len(A)):
        if T[i] == 1:
            score += A[i]
    high = 0
    for i, flag in enumerate(T):
        if flag:
            continue
        else:
            temp = 0
            num = min(n-i, k)
            for l in range(num):
                if T[i+l] == 0:
                    temp += A[i+l]
        high = max(high, temp)
    return score+high


if __name__ == '__main__':
    n, k = [int(i) for i in sys.stdin.readline().split()]
    A = [int(i) for i in sys.stdin.readline().split()]
    T = [int(i) for i in sys.stdin.readline().split()]

    res = fuc(n, k, A, T)
    print(res)

