# https://www.acmicpc.net/problem/15650

from sys import stdin

N, M = map(int, stdin.readline().split())

def NM(check):
    if len(check_set) == M:
        print(" ".join(map(str, check_list)))

        return

    for i in range(check, N + 1):
        if i not in check_set:
            check_set.add(i)
            check_list.append(i)

            NM(i + 1)

            check_set.discard(i)
            check_list.pop()

check_set = set()
check_list = []

NM(1)