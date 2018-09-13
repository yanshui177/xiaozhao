# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace(r' ', r'%20')


if __name__ == '__main__':
    S = Solution()
    print S.replaceSpace('hello world you beach  ')