# -*- coding:utf-8 -*-
"""
函数修饰器：执行当前函数时相当于置换了一个函数入口，这个函数重新调用制定的函数，并且能够执行一些其他的操作，
"""


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2018-3-25')

now()
