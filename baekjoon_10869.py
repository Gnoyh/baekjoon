# https://www.acmicpc.net/problem/10869

import sys

a, b = map(int, sys.stdin.readline().strip().split())

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)