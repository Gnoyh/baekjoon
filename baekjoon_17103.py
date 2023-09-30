# https://www.acmicpc.net/problem/17103

from sys import stdin

T = int(stdin.readline())

input_list = [int(stdin.readline()) for _ in range(T)]

check_list = [1] * (max(input_list) + 1)

def prime(n):
    check_list[0] = 0
    check_list[1] = 0

    for i in range(2, int(n ** 0.5) + 1):
        if check_list[i] == 1:
            for j in range(i * i, n + 1, i):
                check_list[j] = 0

prime(max(input_list))

result_list = [2] + [i for i in range(3, max(input_list) + 1, 2) if check_list[i]]

for i in input_list:
    result = 0

    for j in result_list:
        if j > i // 2:
            break

        if check_list[i - j] == 1:
            result += 1

    print(result)