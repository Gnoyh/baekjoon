# https://www.acmicpc.net/problem/2750

import sys

N = int(sys.stdin.readline())

input_list = []

for i in range(N):
    input_list.append(int(sys.stdin.readline()))

for i in sorted(input_list):
    print(i)