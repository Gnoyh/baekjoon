# https://www.acmicpc.net/problem/1181

import sys

N = int(sys.stdin.readline())

input_list = []

for i in range(N):
    input_str = sys.stdin.readline().strip()

    input_list.append((len(input_str), input_str))

input_list = sorted(set(input_list))

for i in input_list:
    print(i[1])