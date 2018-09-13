#-*- coding:utf-8 -*-
"""
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 65536KB；其他语言 589824KB
题目描述：
一个正整数是素数当且仅当它只含有两个不同的因子，即1和它本身。现在我们定义什么是完美素数。对于一个正整数，我们将它表示成
十进制，然后将它的前𝑥(𝑥≥0)位删去，后𝑦(𝑦≥0)位删去，若剩下的数依然是个素数，且对于所有的合法𝑥,𝑦都成立的话，那么我们称这
个数为完美素数。比如37，它本身是个素数，同时3，7也都是素数，所以37是完美素数。现在你需要求出第n个完美素数。
一个整数𝑛。1≤𝑛≤1000

输出
输出对应的答案，若不存在第n大的完美素数，输出-1。
样例输入
6
样例输出
37
"""


def ana_prime(num):  # 判断是否是素数
    if num == 1 or num == 2:
        return True
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

def ana_perfect(num):  # 判断是否是完美素数
    a = str(num)
    b = set()
    if not ana_prime(num) or len(a)<2:
        return False
    for i in range(1,len(a)):
        for j in range(len(a)):
            right = i+j
            if a[j:right] is not '':
                b.add(int(a[j:right]))
    for i in list(b):
        if not ana_prime(i):
            return False
    return True

def fuc(num):  # 逐一生成数字进行判断
    flag_add = 0
    auto = 1
    while(True):
        auto += 1
        if ana_perfect(auto):
            flag_add += 1
        if num == flag_add:
            return auto

if __name__ == '__main__':
    num = int(raw_input().strip())
    res = fuc(num)
    print res
