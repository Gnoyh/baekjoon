# https://www.acmicpc.net/problem/11653

import sys

N = int(sys.stdin.readline().strip())

while N % 2 == 0:
    print(2)

    N //= 2

for i in range(3, int(N ** 0.5) + 1, 2):
    while N % i == 0:
        print(i)

        N //= i

if N > 1:
    print(N)