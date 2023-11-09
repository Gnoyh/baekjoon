# https://www.acmicpc.net/problem/14889

from sys import stdin

N = int(stdin.readline())

input_list = [[*map(int, stdin.readline().split())] for _ in range(N)]
check_list = [0] * N
start_list = []

check_start = 0

for i in range(N):
    for j in range(N):
        check_list[i] += input_list[i][j] + input_list[j][i]

check_sum = sum(check_list)

result = -1

def startlink(count):
    global result, check_start

    if count == N // 2:

        if result == -1:
            result = abs(check_start - abs(check_sum - check_start)) // 2

        if result > abs(check_start - abs(check_sum - check_start)) // 2:
            result = abs(check_start - abs(check_sum - check_start)) // 2

        return

    for i in range(count, N):
        start_list.append(i)

        check_start += check_list[i]

        startlink(count + 1)

        start_list.pop()

        check_start -= check_list[i]

startlink(0)

print(result)