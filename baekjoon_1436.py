# https://www.acmicpc.net/problem/1436

import sys

N = int(sys.stdin.readline())

check = 666

while N != 0:
    if "666" in str(check):
        N -= 1

        if N == 0:
            break

    check += 1

print(check)