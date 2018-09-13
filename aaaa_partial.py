# -*- coding: utf-8 -*-
"""
偏函数就是修改一个默认参数，固定一个默认的参数
"""
import functools
int2 = functools.partial(int, base=2)

print int2('10111')
