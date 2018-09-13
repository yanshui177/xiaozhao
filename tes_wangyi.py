import sys

def swap(string, a, b):
    if a==b:
        return string
    tempa = string[a]
    tempb = string[b]
    stringa = string[:a] + tempb + string[a+1:]
    stringb = stringa[:b] + tempa + stringa[b+1:]
    return stringb


def fuc(string):
    a = string.split()
    n, m, k = int(a[0]), int(a[1]), int(a[2])
    if n<1 or n>100 or m <1 or m >100 or k<1 or k>1000000000:
        return -1
    flag = 1
    out = 'a'*n+'z'*m
    if k==1:
        return out
    for i in range(n):
        for j in range(m):
            flag += 1
            out1 = swap(out, n-i-1, n+j)
            if flag == k:
                return out1
    if k==flag+1:
        return 'z'*n+'a'*m
    return -1

if __name__ == "__main__":
    string = sys.stdin.readline()
    a = fuc(string)
    print a