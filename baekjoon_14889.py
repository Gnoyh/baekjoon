# https://www.acmicpc.net/problem/14889

from sys import stdin

N = int(stdin.readline())

input_list = [list(map(int, stdin.readline().split())) for _ in range(N)]
check_list = [0] * N
check_set = set()

check = 0

for i in range(N):
    for j in range(N):
        check_list[i] += input_list[i][j] + input_list[j][i]

check_sum = sum(check_list)

int_max = 2147000000
result = int_max

def startlink(count, idx):
    global check, result

    if count == N // 2:
        result = min(result, abs(check - abs(check_sum - check)) // 2)

        return

    for i in range(idx, N):
        if i not in check_set:
            check_set.add(i)

            check += check_list[i]

            startlink(count + 1, i + 1)

            check_set.discard(i)

            check -= check_list[i]

startlink(0, 0)

print(result)