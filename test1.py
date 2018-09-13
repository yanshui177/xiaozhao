import sys


def fuc(line1, line2):
    n, k = int(line1.split()[0]), int(line1.split()[1])
    heights = [int(i) for i in line2.split()]
    maxh = max(heights) - min(heights)

    return 0

if __name__ == "__main__":
    for i in range(2):
        line = sys.stdin.readline()
    a = fuc(line[0], line[1])
    # print a