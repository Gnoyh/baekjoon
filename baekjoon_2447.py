# https://www.acmicpc.net/problem/2447

from sys import stdin

N = int(stdin.readline())
check = 0

while N != 1:
    N = N // 3

    check += 1

def star():
    result_list = [["*"]]

    for i in range(1, check + 1):
        check_list = []

        for j in result_list[i - 1]:
            check_list.append(j * 3)

        for j in result_list[i - 1]:
            check_list.append(j + " " * (3 ** (i - 1)) + j)

        for j in result_list[i - 1]:
            check_list.append(j * 3)

        result_list.append(check_list)

    print("\n".join(result_list[check]))

star()