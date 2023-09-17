# https://www.acmicpc.net/problem/19532

import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

x = (c * e - b * f) // (a * e - b * d)
y = (c * d - a * f) // (b * d - a * e)

print(x, y)