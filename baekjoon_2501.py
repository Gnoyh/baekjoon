# https://www.acmicpc.net/problem/2501

import sys

N, K = map(int, sys.stdin.readline().strip().split())

for i in range(1, N + 1):
    if N % i == 0:
        K -= 1

    if K == 0:
        print(i)

        break
else:
    print(0)