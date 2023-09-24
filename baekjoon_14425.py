# https://www.acmicpc.net/problem/14425

import sys

N, M = map(int, sys.stdin.readline().split())

check_set = set([sys.stdin.readline().strip() for i in range(N)])

input_list = [sys.stdin.readline().strip() for i in range(M)]

result = 0

for i in input_list:
    if i in check_set:
        result += 1

print(result)