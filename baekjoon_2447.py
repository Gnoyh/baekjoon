# https://www.acmicpc.net/problem/2447

from sys import stdin

N = int(stdin.readline())

def star(N):
    if N == 1:
        return "*"
    else:
        check_str = star(N // 3)

    check_list = []

    for i in check_str:
        check_list.append(i * 3)

    for i in check_str:
        check_list.append(i + " " * (N // 3) + i)

    for i in check_str:
        check_list.append(i * 3)

    return check_list

result = star(N)

for i in result:
    print(i)