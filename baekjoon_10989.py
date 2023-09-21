# https://www.acmicpc.net/problem/10989

import sys

N = int(sys.stdin.readline())

check_list = [0 for i in range(10000)]

for i in range(N):
    check_list[int(sys.stdin.readline()) - 1] += 1

for i in range(len(check_list)):
    for j in range(check_list[i]):
        print(i + 1)