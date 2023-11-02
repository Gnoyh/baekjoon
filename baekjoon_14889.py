# https://www.acmicpc.net/problem/14889

from sys import stdin

N = int(stdin.readline())

input_list = [list(map(int, stdin.readline().split())) for _ in range(N)]
check_list = [i for i in range(N)]
visited_list = [0 for i in range(N)]
result_list = []

def calculate():
    check_start = 0
    check_link = 0

    for i in range(N // 2):
        for j in range(i + 1, N // 2):
            if visited_list[i] and visited_list[j]:
                check_start += input_list[i][j] + input_list[j][i]

            elif not visited_list[i] and not visited_list[j]:
                check_link += input_list[i][j] + input_list[j][i]

    result_list.append(abs(check_start - check_link))

def startlink(count):
    if count == N // 2:
        calculate()

        return

    for i in range(count, len(check_list)):
        if not visited_list[i]:
            visited_list[i] = 1

            startlink(count + 1)

            visited_list[i] = 0

startlink(0)

print(min(result_list))