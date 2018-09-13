# -*-coding:utf-8 -*-


def cnt(n):
    dic = {1: 1, 2: 2, 3: 4}
    if n <= 3:
        return dic[n]
    return cnt(n-1) + cnt(n-2) + cnt(n-3)


if __name__ == '__main__':
    print cnt(15)
