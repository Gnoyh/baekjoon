# https://www.acmicpc.net/problem/10871

import sys

N, X = map(int, sys.stdin.readline().strip().split())

input_list = list(map(int, sys.stdin.readline().strip().split()))

for i in range(N):
    if input_list[i] < X:
        print(input_list[i], end=" ")