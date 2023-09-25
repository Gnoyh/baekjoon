# https://www.acmicpc.net/problem/1620

import sys

N, M = map(int, sys.stdin.readline().split())

name_dict = {sys.stdin.readline().strip(): i for i in range(1, N + 1)}
num_dict = {v: k for k, v in name_dict.items()}

for i in range(M):
    check = sys.stdin.readline().strip()

    if check.isdigit():
        print(num_dict.get(int(check)))
    else:
        print(name_dict.get(check))