# https://www.acmicpc.net/problem/10810

import sys

N, M = map(int, sys.stdin.readline().strip().split())

result_list = [0 for i in range(N)]

for x in range(M):
    i, j, k = map(int, sys.stdin.readline().strip().split())

    for y in range(i, j + 1):
        result_list[y - 1] = k

for i in range(N):
    if i == N - 1:
        print(result_list[i])
    else:
        print(result_list[i], end=" ")