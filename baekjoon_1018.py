# https://www.acmicpc.net/problem/1018

import sys

N, M = map(int, sys.stdin.readline().split())

input_list = []
comp_list = ['B', 'W']

B_list = []
W_list = []

for i in range(N):
    input_list.append(sys.stdin.readline().strip())

for h in range(2):
    comp = h

    for i in range(N):
        check_list = []

        for j in range(7, M):
            check = 0

            for k in range(j - 7, j + 1):
                if comp_list[comp] != input_list[i][k]:
                    check += 1

                comp = abs(comp - 1)

            check_list.append(check)

        if h == 0:
            B_list.append(check_list)
        else:
            W_list.append(check_list)

BW_list = []
WB_list = []

for i in range(N):
    if i % 2 == 0:
        BW_list.append(B_list[i])
        WB_list.append(W_list[i])
    else:
        BW_list.append(W_list[i])
        WB_list.append(B_list[i])

result = 65

for i in range(len(BW_list[0])):
    for j in range(7, N):
        sum_BW = 0
        sum_WB = 0

        for k in range(j - 7, j + 1):
            sum_BW += BW_list[k][i]
            sum_WB += WB_list[k][i]

        if sum_BW < result:
            result = sum_BW

        if sum_WB < result:
            result = sum_WB

print(result)