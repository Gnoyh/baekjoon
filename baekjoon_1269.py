# https://www.acmicpc.net/problem/1269

import sys

A, B = map(int, sys.stdin.readline().split())

input_list = []

for i in range(2):
    input_list += list(map(int, sys.stdin.readline().split()))

print(len(set(input_list)) * 2 - (A + B))