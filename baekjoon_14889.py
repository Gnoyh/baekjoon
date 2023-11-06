# https://www.acmicpc.net/problem/14889

import sys

N = int(sys.stdin.readline())

input_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited_list = [False] * N

result = sys.maxsize

def startlink(count):
    global result

    if count == N // 2:
        check_start = 0
        check_link = 0

        for i in range(N):
            for j in range(i + 1, N):
                if visited_list[i] and visited_list[j]:
                    check_start += input_list[i][j] + input_list[j][i]

                if not visited_list[i] and not visited_list[j]:
                    check_link += input_list[i][j] + input_list[j][i]

        if result > abs(check_start - check_link):
            result = abs(check_start - check_link)

        return

    for i in range(count, N):
        if not visited_list[i]:
            visited_list[i] = True

            startlink(count + 1)

            visited_list[i] = False

startlink(0)

print(result)