#-*- coding:utf-8 -*-
"""
3 4
.OXO
O..O
.XOX
"""


def fuc(S, shape):
    result = ''
    for i in range(S[0]-1, -1, -1):
        for j in range(S[1]):
            if i == S[0]-1:  # 最后一行
                if shape[i][j] == 'o':
                    shape[i][j] = '.'
            else:  # 其他行
                for ii in range(i,S[0]):
                    for jj in range(S[1]):
                        if ii == S[0] - 1:  # 最后一行
                            if shape[ii][jj] == 'o':
                                shape[ii][jj] = '.'
                        elif shape[ii][jj] == 'o' and shape[ii+1][jj] == '.':
                            shape[ii][jj], shape[ii + 1][jj] = '.', 'o'
                        else:
                            pass
    for i in range(S[0]):
        result += ''.join(shape[i]) + '\n'
    return result[:-1]


if __name__ == '__main__':
    S = [int(i) for i in raw_input().strip().split()]
    shape = []
    for i in range(S[0]):
        temp = []
        A = raw_input().strip()
        for j in range(S[1]):
            temp.append(A[j])
        shape.append(temp)
    res = fuc(S, shape)
    print res