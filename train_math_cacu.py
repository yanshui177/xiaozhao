#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

今天上课，老师教了小易怎么计算加法和乘法，乘法的优先级大于加法，但是如果一个运算加了括号，那么它的优先级是最高的。例如：
1  1+2*3=7
2  1*(2+3)=5
3  1*2*3=6
4  (1+2)*3=9
现在小易希望你帮他计算给定3个数a，b，c，在它们中间添加"+"， "*"， "("， ")"符号，能够获得的最大值。
"""


def max2(a, b):
    return max(a+b, a*b)


def max3(a, b, c):
    return max(max2(max2(a, b), c), max2(a, max2(b, c)))


if __name__ == '__main__':
    a, b, c = [int(i) for i in raw_input().strip().split()]
    res = max3(a, b, c)
    print res

