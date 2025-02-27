# https://www.acmicpc.net/problem/10813

import sys
import copy

N, M = map(int, sys.stdin.readline().strip().split())

result_list = [i + 1 for i in range(N)]

for x in range(M):
    check_list = copy.deepcopy(result_list)

    i, j = map(int, sys.stdin.readline().strip().split())

    check_list[i - 1] = result_list[j - 1]
    check_list[j - 1] = result_list[i - 1]

    result_list = check_list

for i in range(N):
    if i == N - 1:
        print(result_list[i])
    else:
        print(result_list[i], end=" ")