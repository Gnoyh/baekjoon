# https://www.acmicpc.net/problem/11866

from sys import stdin

N, K = map(int, stdin.readline().split())

def josephus():
    input_list = list(str(i) for i in range(1, N + 1))
    result_list = list()

    check = 0

    while input_list:
        check += K - 1
        check = check % len(input_list)

        result_list.append(input_list.pop(check))

    print("<" + ", ".join(result_list), end=">")

josephus()