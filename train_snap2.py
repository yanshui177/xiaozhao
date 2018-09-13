#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
题目：小明容易犯困，上面是对他感兴趣的分数，下面是是否犯困
10 3
1 3 5 2 5 4 1 3 5 6
1 1 0 1 0 0 1 0 1 0
"""
n, k = map(int, raw_input().strip().split())
a = map(int, raw_input().strip().split())
b = map(int, raw_input().strip().split())
ans1 =0
for i in range(n):  # 先计算的是直接得到的总分数
    if b[i] == 1:
        ans1 += a[i]
        a[i] =0
print("a:", a)
ans2 =0  # 再计算能得到的最高的分数
for i in range(1, n):
    a[i] += a[i-1]
print("a:", a)
for i in range(k):
    ans2 =max(ans2, a[i])
print('ans2:', ans2, k, n )
for i in range(k, n):
    ans2 =max(ans2, a[i]-a[i-k])
print('ans2:', ans2, k, n)
print ans1+ans2