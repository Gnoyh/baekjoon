# https://www.acmicpc.net/problem/2231

import sys

N = sys.stdin.readline()

result = 0

max_int = int(N[0]) - 1 + 9 * (len(N) - 2)

for i in range(max_int, 0, -1):
    check = int(N) - i

    if i == sum(list(map(int, str(check)))):
        result = check

        break

print(result)