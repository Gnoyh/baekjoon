# https://www.acmicpc.net/problem/9663

from sys import stdin

N = int(stdin.readline())

result = 0

def nqueen(check, check_second, check_third):
    global result
    global check_first

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
                check_first[i] = True
                check_second[i] = True
                check_third[i] = True

                nqueen(check + 1, check_second[1: ] + [False], [False] + check_third[: -1])

                check_first[i] = False
                check_second[i] = False
                check_third[i] = False

check_first = [False] * N

nqueen(0, [False] * N, [False] * N)

print(result)