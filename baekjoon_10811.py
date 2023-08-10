# https://www.acmicpc.net/problem/10811

import copy

N, M = map(int, input().split())

result_list = [i + 1 for i in range(N)]

for x in range(M):
    check_list = copy.deepcopy(result_list)

    i, j = map(int, input().split())

    for y in range(i, j + 1):
        check_list[y - 1] = result_list[i + j - y - 1]

    result_list = check_list

for i in range(N):
    print(result_list[i], end=" ")