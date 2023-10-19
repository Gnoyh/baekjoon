# https://www.acmicpc.net/problem/2447

from sys import stdin

N = int(stdin.readline())

def star():
    result_list = [["*"]]

    check = 1

    while (3 ** check) <= N:
        check_list = []

        for j in result_list[check - 1]:
            check_list.append(j * 3)

        for j in result_list[check - 1]:
            check_list.append(j + " " * (3 ** (check - 1)) + j)

        for j in result_list[check - 1]:
            check_list.append(j * 3)

        result_list.append(check_list)

        check += 1

    print("\n".join(result_list[check - 1]))

star()