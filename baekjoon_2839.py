# https://www.acmicpc.net/problem/2839

import sys

N = int(sys.stdin.readline())

check_set = set()

if N % 3 == 0:
    check_set.add(N // 3)

if N % 5 == 0:
    check_set.add(N // 5)

for i in range(1, N // 3 + 1):
    if (N - (3 * i)) % 5 == 0:
        check_set.add(i + (N - (3 * i)) // 5)

if len(check_set) == 0:
    print(-1)
else:
    print(min(check_set))