# https://www.acmicpc.net/problem/10815

import sys

N = int(sys.stdin.readline())

N_list = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

M_list = list(map(int, sys.stdin.readline().split()))

M_dict = {M_list[i]: i for i in range(M)}

result_list = [0] * M

for i in range(N):
    check = M_dict.get(N_list[i])

    if check != None:
        result_list[check] = 1

for i in result_list:
    print(i, end=" ")