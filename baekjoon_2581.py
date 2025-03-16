# https://www.acmicpc.net/problem/2581

import sys

M = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())

result_sum = 0
result_min = 0

check_list = [1 for i in range(N + 1)]

check_list[0] = 0
check_list[1] = 0

for i in range(4, N + 1, 2):
    check_list[i] = 0

for i in range(3, int(N ** 0.5) + 1, 2):
    if check_list[i] == 1:
        for j in range(i * 3, N + 1, i):
            check_list[j] = 0

for i in range(M, N + 1):
    if check_list[i] == 1:
        result_sum += i

        if result_min == 0:
            result_min = i

if result_sum != 0:
    print(result_sum)
    print(result_min)
else:
    print(-1)