# https://www.acmicpc.net/problem/2292

import sys

N = int(sys.stdin.readline().strip())

N -= 1
result = 1

while True:
    if N < 1:
        break
    else:
        N -= 6 * result
        result += 1

print(result)