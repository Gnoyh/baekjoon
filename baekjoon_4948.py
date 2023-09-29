# https://www.acmicpc.net/problem/4948

from sys import stdin

input_list = list()

while True:
    n = int(stdin.readline())

    if n == 0:
        break
    else:
        input_list.append(n)

def prime(input_list, n):
    check_list = [1] * (n + 1)

    check_list[0] = 0
    check_list[1] = 0

    for i in range(2, int(n ** 0.5) + 1):
        if check_list[i] == 1:
            for j in range(i * i, n + 1, i):
                check_list[j] = 0

    for i in input_list:
        check = 0

        for j in range(i + 1, i * 2 + 1):
            if check_list[j] == 1:
                check += 1

        print(check)

check_list = prime(input_list, max(input_list) * 2 + 1)