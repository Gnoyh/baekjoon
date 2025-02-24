# https://www.acmicpc.net/problem/1193

import sys

X = int(sys.stdin.readline().strip())

check = 1
i = 1

result_a = 0
result_b = 0

while True:
    if X <= i:
        if i % 2 == 0:
            result_a = X
            result_b = i + 1 - X
        else:
            result_a = i + 1 - X
            result_b = X

        break
    else:
        X -= check

        check += 1
        i += 1

print("%d/%d" % (result_a, result_b))