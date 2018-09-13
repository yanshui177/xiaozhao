#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
又到了周末，小易的房间乱得一团糟。
他希望将地上的杂物稍微整理下，使每团杂物看起来都紧凑一些，没有那么乱。
地上一共有n团杂物，每团杂物都包含4个物品。第i物品的坐标用(ai,bi)表示，小易每次都可以将它绕着(xi,yi)逆时针旋转，
这将消耗他的一次移动次数。如果一团杂物的4个点构成了一个面积不为0的正方形，我们说它是紧凑的。
因为小易很懒，所以他希望你帮助他计算一下每团杂物最少需要多少步移动能使它变得紧凑。
"""


def change(i, x, y):
    return [x + y - i[1], y - x + i[0]]


def dis(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def square(a, b, c, d):
    q = [dis(a, b), dis(a, c), dis(a, d), dis(b, c), dis(b, d), dis(c, d)]
    q.sort()
    if q[0] != 0 and q[0] == q[1] and q[1] == q[2] and q[2] == q[3] and q[4] == q[5] and q[4] == 2 * q[3]:
        return True
    return False

n = int(raw_input().strip())
for w in range(n):
    best = 100
    p = []
    for i in range(4):
        a, b, x, y = map(int, raw_input().strip().split())
        temp1 = [[a, b]]
        for j in range(3):
            temp1.append(change(temp1[-1], x, y))
        p.append(temp1)

    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if square(p[0][i], p[1][j], p[2][k], p[3][l]):
                        best = min(best, i + j + k + l)
    if best == 100:
        best = -1
    print best