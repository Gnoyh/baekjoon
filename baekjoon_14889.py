# https://www.acmicpc.net/problem/14889

from sys import stdin

N = int(stdin.readline())

input_list = [list(map(int, stdin.readline().split())) for _ in range(N)]
check_list = [i for i in range(N)]
check_set = set()

result_list = []

check_start = 0

def startlink(count):
    global check_start

    if count == N // 2:
        check_link = 0

        check_linklist = [i for i in check_list if i not in check_set]

        for i in range(N // 2):
            for j in range(i + 1, N // 2):
                check_link += input_list[check_linklist[i]][check_linklist[j]] + input_list[check_linklist[j]][check_linklist[i]]

        result_list.append(abs(check_start - check_link))

        return

    for i in range(count, len(check_list)):
        if check_list[i] not in check_set:
            check = 0

            for j in check_set:
                check += input_list[i][j] + input_list[j][i]

            check_start += check
            check_set.add(check_list[i])

            startlink(count + 1)

            check_start -= check
            check_set.discard(check_list[i])

startlink(0)

print(min(result_list))