# https://www.acmicpc.net/problem/10813

import copy

N, M = map(int, input().split())

result_list = [i + 1 for i in range(N)]

for x in range(M):
    check_list = copy.deepcopy(result_list)

    i, j = map(int, input().split())

    check_list[i - 1] = result_list[j - 1]
    check_list[j - 1] = result_list[i - 1]

    result_list = check_list

for i in range(N):
    if i == N - 1:
        print(result_list[i])
    else:
        print(result_list[i], end=" ")