# https://www.acmicpc.net/problem/11650

import sys

N = int(sys.stdin.readline())

input_list = []

for i in range(N):
    input_list.append(list(map(int, sys.stdin.readline().split())))

input_list.sort()

for i in input_list:
    print(i[0], i[1])