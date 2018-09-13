#-*- coding:utf-8 -*-
"""
可能IP
"""
import itertools
import re


def check_ip(ipAddr):
  compile_ip=re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
  if compile_ip.match(ipAddr):
    return True
  else:
    return False

def fuc(string):
    address = []
    for i in list(itertools.combinations(list(range(len(string))), 3)):
        temp = []
        i = list(i)
        temp.append(string[0:i[0]])
        temp.append(string[i[0]:i[1]])
        temp.append(string[i[1]:i[2]])
        temp.append(string[i[2]:len(string)])
        address.append('.'.join(temp))
    num = 0
    for i in address:
        if check_ip(i):
            num+=1
    return num
    # return list(itertools.combinations(list(range(len(string))), 3))


if __name__ == '__main__':
    string = raw_input().strip()
    res = fuc(string)

    print res