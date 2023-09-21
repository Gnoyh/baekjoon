# https://www.acmicpc.net/problem/11651

import sys

N = int(sys.stdin.readline())

input_list = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    input_list.append((y, x))

input_list.sort()

for i in input_list:
    print(i[1], i[0])