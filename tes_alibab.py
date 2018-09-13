import sys


def Solve(N, M, map):
    # for i in range(len(map)):
    #     for j in range(len(map)):
    #         if map[i][j] == map[j][i]:
    #             raise TypeError(r"The matrix 'map' is wrong!!!")
    #     print i
    res = []
    for i in range(len(map)):
        temp_l = 0
        for j in range(i, len(map)):
            temp_l += map[i][j]
        res.append(temp_l)
    return res

if __name__ == "__main__":
    # input
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    size = sys.stdin.readline()
    map = []
    for i in range(int(size[0])):
        line = sys.stdin.readline()
        map.append([int(temp) for temp in line.split()])

    # solve
    res = Solve(N, M, map)
    print(res)

