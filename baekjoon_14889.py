# https://www.acmicpc.net/problem/14889

from sys import stdin

N = int(stdin.readline())

input_list = [list(map(int, stdin.readline().split())) for _ in range(N)]

result = 0
result_min = -1

def startlink(check_list, check_set, check):
    global result
    global result_min

    if len(check_set) == N // 2:
        if result == 0:
            result = check

            startlink([i for i in check_list if i not in check_set], set(), 0)

            return
        else:
            if result_min == -1:
                result_min = abs(result - check)
            else:
                if result_min > abs(result - check):
                    result_min = abs(result - check)

            result = 0

            return

    for i in check_list:
        if i not in check_set:
            for j in check_set:
                check += input_list[i][j] + input_list[j][i]

            check_set.add(i)

            startlink(check_list, check_set, check)

            check_set.discard(i)

startlink([i for i in range(N)], set(), 0)