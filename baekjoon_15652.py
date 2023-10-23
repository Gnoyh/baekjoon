# https://www.acmicpc.net/problem/15652

from sys import stdin

N, M = map(int, stdin.readline().split())

def NM(check):
    if len(check_list) == M:
        print(" ".join(map(str, check_list)))

        return

    for i in range(check, N + 1):
        check_list.append(i)

        NM(i)

        check_list.pop()

check_list = []

NM(1)