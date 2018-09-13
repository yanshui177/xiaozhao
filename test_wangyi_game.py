# -*- coding:utf-8 -*-
import sys

"""
题目要求：完美世界的题，上一行是面试者到来的时间，下面一行是走的时间，第一个是面试者总数，问：最多的时候需要几个
面试官

这是用来输入的
6
900 940 950 1100 1500 1800
930 1200 1120 1130 1900 2000
"""


def fuc(N, arrive, leave):
    stack1 = [arrive[0]]
    stack2 = [leave[0]]
    length = 1
    for i in range(1, N-1):  # 对每个面试者进行考察
        temp = []  # 设定临时变量，用于存储需要删除的面试者
        for num, time in enumerate(stack2):  # 比较离去时间，如果下一个面试者到来时间比之前这些面试者晚，那就得删除
            if arrive[i] < time:
                temp.append(num)
        for d in temp:
            stack1.pop(d)
            stack2.pop(d)

        stack1.append(arrive[i])  # 加入新的面试者
        stack2.append(leave[i])
        length = len(stack1) if length < len(stack1) else length
    return length

if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    arrive = [int(i) for i in sys.stdin.readline().strip().split()]
    leave = [int(i) for i in sys.stdin.readline().strip().split()]
    a = fuc(N, arrive, leave)
    print a