# https://www.acmicpc.net/problem/9663

from sys import stdin

N = int(stdin.readline())

result = 0

def nqueen(check):
    global result
    global check_first
    global check_second
    global check_third

    if check == N:
        result += 1

        return

    for i in range(N):
        if check_first[i]:
            continue
        else:
            if check_second[i] or check_third[i]:
                continue
            else:
                check_secondid = check_second[0]
                check_thirdid = check_third[-1]

                check_first[i] = True
                check_second[i] = True
                check_third[i] = True

                check_second = check_second[1: ] + [False]
                check_third = [False] + check_third[: -1]

                nqueen(check + 1)

                check_second = [check_secondid] + check_second[: -1]
                check_third = check_third[1: ] + [check_thirdid]

                check_first[i] = False
                check_second[i] = False
                check_third[i] = False

check_first = [False] * N
check_second = [False] * N
check_third = [False] * N

nqueen(0)

print(result)