# https://www.acmicpc.net/problem/22864

import sys

a, b, c, m = map(int, sys.stdin.readline().strip().split())

check = 0
result = 0

for i in range(24):
    if check + a <= m:
        check += a
        result += b
    else:
        if check - c < 0:
            check = 0
        else:
            check -= c

if a > m:
    print(0)
else:
    print(result)