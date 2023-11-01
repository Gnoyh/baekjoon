# https://www.acmicpc.net/problem/14889

from sys import stdin

N = int(stdin.readline())

input_list = [list(map(int, stdin.readline().split())) for _ in range(N)]

check = 0
result = 0
result_min = -1

def startlink(check_list, check_set, count):
    global check
    global result
    global result_min

    if count == N // 2:
        check = 0

        for i in check_set:
            for j in check_set:
                if i != j:
                    check += input_list[i][j]

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

    for i in range(count, len(check_list)):
        if check_list[i] not in check_set:
            check_set.add(check_list[i])

            startlink(check_list, check_set, count + 1)

            check_set.discard(check_list[i])

startlink([i for i in range(N)], set(), 0)

print(result_min)