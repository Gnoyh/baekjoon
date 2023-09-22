# https://www.acmicpc.net/problem/10815

import sys

N = int(sys.stdin.readline())

N_set = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

M_list = list(map(int, sys.stdin.readline().split()))

for i in M_list:
    if i in N_set:
        print(1, end=" ")
    else:
        print(0, end=" ")