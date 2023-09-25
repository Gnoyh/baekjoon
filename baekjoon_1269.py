# https://www.acmicpc.net/problem/1269

import sys

A_size, B_size = map(int, sys.stdin.readline().split())

A_set = set(map(int, sys.stdin.readline().split()))
B_set = set(map(int, sys.stdin.readline().split()))

count = 0

if A_size < B_size:
    for i in A_set:
        if i in B_set:
            count += 1
else:
    for i in B_set:
        if i in A_set:
            count += 1

print(A_size + B_size - count * 2)