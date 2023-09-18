# https://www.acmicpc.net/problem/1018

import sys

N, M = map(int, sys.stdin.readline().split())

input_list = [sys.stdin.readline().strip() for i in range(N)]
check_list = [[0 for j in range(M)] for i in range(N)]

for i in range(N):
    for j in range(M):
        if ((i + j) % 2 == 0 and input_list[i][j] == "W") or ((i + j) % 2 == 1 and input_list[i][j] == "B"):
            check_list[i][j] = 1

result_list = []

for i in range(N - 7):
    for j in range(M - 7):
        check = 0

        for k in range(i, i + 8):
            check += sum(check_list[k][j : j + 8])

        result_list.append(check)

if min(result_list) < 64 - max(result_list):
    print(min(result_list))
else:
    print(64 - max(result_list))