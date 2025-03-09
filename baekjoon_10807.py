# https://www.acmicpc.net/problem/10807

import sys

N = int(sys.stdin.readline().strip())

input_list = list(map(int, sys.stdin.readline().strip().split()))

v = int(sys.stdin.readline().strip())

count = 0

for i in range(N):
    if input_list[i] == v:
        count += 1

print(count)