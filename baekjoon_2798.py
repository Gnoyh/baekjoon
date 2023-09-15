# https://www.acmicpc.net/problem/2798

import sys

N, M = map(int, sys.stdin.readline().split())

check_list = list(map(int, input().split()))

result = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if check_list[i] + check_list[j] + check_list[k] > result and check_list[i] + check_list[j] + check_list[k] <= M:
                result = check_list[i] + check_list[j] + check_list[k]

print(result)