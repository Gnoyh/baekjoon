# https://www.acmicpc.net/problem/15552

import sys

num = int(input())

for i in range(num):
    a, b = map(int, sys.stdin.readline().split())

    print(a + b)