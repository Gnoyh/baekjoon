# https://www.acmicpc.net/problem/10814

import sys

N = int(sys.stdin.readline())

input_list = []

for i in range(N):
    age, name = map(str, sys.stdin.readline().strip().split())

    input_list.append((int(age), name))

input_list.sort(key=lambda x: x[0])

for i in input_list:
    print(i[0], i[1])