#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
又到了丰收的季节，恰逢小易去牛牛的果园里游玩。
牛牛常说他对整个果园的每个地方都了如指掌，小易不太相信，所以他想考考牛牛。
在果园里有N堆苹果，每堆苹果的数量为ai，小易希望知道从左往右数第x个苹果是属于哪一堆的。
牛牛觉得这个问题太简单，所以希望你来替他回答。
"""


def fun(N, A, x):
    for i in range(1, N):
        A[i] += A[i-1]
        if A[i] >= x:
            return i+1
    return 0

if __name__ == '__main__':
    N = int(raw_input().strip())
    A = [int(i) for i in raw_input().strip().split()]
    x = int(raw_input().strip())

    print N, A
    res = fun(N, A, x)
    print(res)