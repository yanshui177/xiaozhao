#-*- coding:utf-8 -*-
"""

"""
from math import ceil


def fuc(HP, NA, BA):
    n = 0
    if BA > 2*NA:
        n = int(ceil(float(HP) / BA))*2
        temp = HP%BA
        if int(ceil(float(temp) / NA)) < 2:
            n -= 1
    else:
        n = int(ceil(float(HP) / float(NA)))
    return n


if __name__ == '__main__':
    HP = int(raw_input().strip())
    NA = int(raw_input().strip())
    BA = int(raw_input().strip())
    res = fuc(HP, NA, BA)
    print res