# https://www.acmicpc.net/problem/1764

import sys

N, M = map(int, sys.stdin.readline().split())

N_set = set(sys.stdin.readline().strip() for i in range(N))

check_list = []

for i in range(M):
    check = sys.stdin.readline().strip()

    if check in N_set:
        check_list.append(check)

print(len(check_list))
print("\n".join(sorted(check_list)))