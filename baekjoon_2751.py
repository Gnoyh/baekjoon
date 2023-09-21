# https://www.acmicpc.net/problem/2751

import sys

N = int(sys.stdin.readline())

input_list = []

for i in range(N):
    input_list.append(int(sys.stdin.readline()))

input_list.sort()

for i in input_list:
    print(i)