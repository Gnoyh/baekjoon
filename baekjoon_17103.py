# https://www.acmicpc.net/problem/17103

from sys import stdin

T = int(stdin.readline())

input_list = [int(stdin.readline()) for _ in range(T)]

def prime(n):
    check_list = [1] * (n + 1)

    check_list[0] = 0
    check_list[1] = 0

    for i in range(2, int(n ** 0.5) + 1):
        if check_list[i] == 1:
            for j in range(i * i, n + 1, i):
                check_list[j] = 0

    return check_list

check_list = prime(max(input_list))

for i in input_list:
    result = 0

    if i == 4:
        result += 1

    for j in range(3, i // 2 + 1, 2):
        if check_list[j] + check_list[i - j] == 2:
            result += 1

    print(result)