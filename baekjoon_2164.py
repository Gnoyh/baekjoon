# https://www.acmicpc.net/problem/2164

from sys import stdin

N = int(stdin.readline())

input_list = list(i for i in range(1, N + 1))

def card(input_list, n):
    check_list = list()

    if n % 2 == 1:
        check_list.append(input_list[-1])

    for i in range(1, n, 2):
        check_list.append(input_list[i])

    if len(check_list) == 1:
        print(check_list[0])
    else:
        card(check_list, len(check_list))

card(input_list, N)