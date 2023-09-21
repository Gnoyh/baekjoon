# https://www.acmicpc.net/problem/1427

import sys

N = sys.stdin.readline().strip()

input_list = list(N)
input_list.sort(reverse=True)

for i in input_list:
    print(i, end="")