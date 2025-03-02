# https://www.acmicpc.net/problem/10818

import sys

N = int(sys.stdin.readline().strip())

input_list = list(map(int, sys.stdin.readline().strip().split()))

result_min = 1000001
result_max = -1000001

for i in range(N):
    if input_list[i] < result_min:
        result_min = input_list[i]

    if input_list[i] > result_max:
        result_max = input_list[i]

print(result_min, result_max)