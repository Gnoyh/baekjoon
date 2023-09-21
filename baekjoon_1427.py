# https://www.acmicpc.net/problem/1427

import sys

N = sys.stdin.readline().strip()

for i in sorted(N, reverse=True):
    print(int(i), end="")