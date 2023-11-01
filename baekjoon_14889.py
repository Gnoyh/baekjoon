# https://www.acmicpc.net/problem/14889

from sys import stdin

N = int(stdin.readline())

input_list = [list(map(int, stdin.readline().split())) for _ in range(N)]
check_list = [i for i in range(N)]
check_set = set()

result = -1

def startlink(count):
    global result

    if count == N // 2:
        check_start = 0
        check_link = 0

        check_startlist = list(check_set)
        check_linklist = [i for i in check_list if i not in check_set]

        for i in range(N // 2):
            for j in range(i + 1, N // 2):
                check_start += input_list[check_startlist[i]][check_startlist[j]] + input_list[check_startlist[j]][check_startlist[i]]

        for i in range(N // 2):
            for j in range(i + 1, N // 2):
                check_link += input_list[check_linklist[i]][check_linklist[j]] + input_list[check_linklist[j]][check_linklist[i]]

        if result == -1:
            result = abs(check_start - check_link)
        else:
            if result > abs(check_start - check_link):
                result = abs(check_start - check_link)

        return

    for i in range(count, len(check_list)):
        if check_list[i] not in check_set:
            check_set.add(check_list[i])

            startlink(count + 1)

            check_set.discard(check_list[i])

startlink(0)

print(result)