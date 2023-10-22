# https://www.acmicpc.net/problem/15651

from sys import stdin

N, M = map(int, stdin.readline().split())

def NM():
    if len(check_list) == M:
        print(" ".join(map(str, check_list)))

        return

    for i in range(1, N + 1):
        check_list.append(i)

        NM()

        check_list.pop()

check_list = []

NM()