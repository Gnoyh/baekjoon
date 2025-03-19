# https://www.acmicpc.net/problem/5597

import sys

check_list = [0 for i in range(30)]

for i in range(28):
    n = int(sys.stdin.readline().strip())

    check_list[n - 1] = 1

for i in range(30):
    if check_list[i] == 0:
        print(i + 1)