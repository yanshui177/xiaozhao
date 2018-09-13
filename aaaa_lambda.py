# -*- coding: utf-8 -*-
"""
lambda函数就是设定一个匿名函数，没有函数名称
"""
import functools

C = [39.2, 36.5, 37.3, 38, 37.8]
F = list(map(lambda x: (float(9)/5)*x + 32, C))
print(F)

# 使用了filter
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
odd_numbers = list(filter(lambda x: x % 2, fibonacci))
print(odd_numbers)

print(functools.reduce(lambda x,y: x+y, [47,11,42,13]))
# 累加
from functools import reduce
# 找到最大值
f = lambda a,b: a if (a > b) else b
print(reduce(f, [47, 11, 42, 102,13]))
# 累乘
print(reduce(lambda x, y: x*y, range(1,3)))
m = list(range(1,3))
# [1, 2]
print(m)