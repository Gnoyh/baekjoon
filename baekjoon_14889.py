# https://www.acmicpc.net/problem/14889

import sys

N = int(sys.stdin.readline())

input_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited_list = [False] * N
check_list = [i for i in range(N)]
start_list = []

result = sys.maxsize

def startlink(count):
    global result

    if count == N // 2:
        check_start = 0
        check_link = 0

        link_list = [i for i in check_list if i not in start_list]

        for i in range(N // 2):
            for j in range(i + 1, N // 2):
                check_start += input_list[start_list[i]][start_list[j]] + input_list[start_list[j]][start_list[i]]
                check_link += input_list[link_list[i]][link_list[j]] + input_list[link_list[j]][link_list[i]]

        if result > abs(check_start - check_link):
            result = abs(check_start - check_link)

        return

    for i in range(count, N):
        if not visited_list[i]:
            visited_list[i] = True

            start_list.append(i)

            startlink(count + 1)

            visited_list[i] = False

            start_list.remove(i)

startlink(0)

print(result)