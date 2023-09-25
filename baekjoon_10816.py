# https://www.acmicpc.net/problem/10816

import sys

N = int(sys.stdin.readline())

N_list = list(map(int, sys.stdin.readline().split()))
N_dict = dict()

for i in N_list:
    if i in N_dict:
        N_dict[i] += 1
    else:
        N_dict[i] = 1

M = int(sys.stdin.readline())

M_list = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    if M_list[i] in N_dict:
        M_list[i] = str(N_dict[M_list[i]])
    else:
        M_list[i] = "0"

print(" ".join(M_list))