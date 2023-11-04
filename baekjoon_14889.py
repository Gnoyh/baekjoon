# https://www.acmicpc.net/problem/14889

import sys
from sys import stdin

N = int(stdin.readline())

input_list = [list(map(int, stdin.readline().split())) for _ in range(N)]
check_list = [i for i in range(N)]
visited_list = [0 for i in range(N)]

result = sys.maxsize

def calculate():
    global result

    start_list = []
    link_list = []

    check_start = 0
    check_link = 0

    for i in range(N):
        if visited_list[i] == 1:
            start_list.append(i)
        else:
            link_list.append(i)

    for i in range(N // 2):
        for j in range(i + 1, N // 2):
            check_start += input_list[start_list[i]][start_list[j]] + input_list[start_list[j]][start_list[i]]
            check_link += input_list[link_list[i]][link_list[j]] + input_list[link_list[j]][link_list[i]]

    if result > abs(check_start - check_link):
        result = abs(check_start - check_link)

def startlink(count):
    if count == N // 2:
        calculate()

        return

    for i in range(count, N):
        if visited_list[i] == 0:
            visited_list[i] = 1

            startlink(count + 1)

            visited_list[i] = 0

startlink(0)

print(result)