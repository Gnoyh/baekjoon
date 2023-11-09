# https://www.acmicpc.net/problem/14889

from sys import stdin

N = int(stdin.readline())

input_list = [[*map(int, stdin.readline().split())] for _ in range(N)]
check_list = [0] * N
check_set = set()

for i in range(N):
    for j in range(N):
        check_list[i] += input_list[i][j] + input_list[j][i]

check_sum = sum(check_list)

result = -1

def startlink(count):
    global result

    check = 0

    if count == N // 2:
        for i in check_set:
            check += check_list[i]

        if result == -1:
            result = abs(check - abs(check_sum - check)) // 2

        if result > abs(check - abs(check_sum - check)) // 2:
            result = abs(check - abs(check_sum - check)) // 2

        return

    for i in range(count, N):
        if i not in check_set:
            check_set.add(i)

            startlink(count + 1)

            check_set.discard(i)

startlink(0)

print(result)