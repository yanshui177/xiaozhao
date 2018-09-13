#-*- coding:utf-8 -*-


def fuc(A, B):
    if A%B==0 or B%2==0 or B%5==0:
        aa = len(str(float(A)/B).split('.')[-1])
        return str(aa)+' 0'
    else:
        tmps = str(float(A)/B).split('.')[-1]
        pos = 0
        for i in range(0, 20):
            for j in range(i,20):
                if tmps[i:j] == tmps[j:2*j-i] and tmps[j:2*j-i] == tmps[2*j-i:3*j-2*i]:
                    pos = i
                    break
        return str(i) + ' ' + str(pos)

if __name__ == '__main__':
    S = [int(i) for i in raw_input().strip().split()]
    res = fuc(S[0], S[1])
    print res