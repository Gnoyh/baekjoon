# https://www.acmicpc.net/problem/24267

import sys

n = int(sys.stdin.readline())

print(n * (n - 1) * (n - 2) // 6)
print(3)