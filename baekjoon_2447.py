# https://www.acmicpc.net/problem/2447

from sys import stdin
from math import log

N = int(log(int(stdin.readline()), 3))

def star(N):
    if N == 0:
        return "*"
    else:
        check_str = star(N - 1)

    check_list = []

    for i in check_str:
        check_list.append(i * 3)

    for i in check_str:
        check_list.append(i + " " * 3 ** (N - 1) + i)

    for i in check_str:
        check_list.append(i * 3)

    return check_list

print("\n".join(star(N)))