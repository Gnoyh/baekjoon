# https://www.acmicpc.net/problem/1929

from sys import stdin

M, N = map(int, stdin.readline().split())

check_list = [1 for i in range(N + 1)]

check_list[0] = 0
check_list[1] = 0

for i in range(2, int(N ** 0.5) + 1):
    if check_list[i] == 1:
        for j in range(i * i, N + 1, i):
            check_list[j] = 0

for i in range(M, N + 1):
    if check_list[i] == 1:
        print(i)