# https://www.acmicpc.net/problem/24313

import sys

a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())

if (a1 * n0 + a0 > c * n0) or (a1 * 100 + a0 > c * 100):
    print(0)
else:
    print(1)