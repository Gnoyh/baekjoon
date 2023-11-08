# https://www.acmicpc.net/problem/9663

from sys import stdin

N = int(stdin.readline())

result = 0

def truefalse(i, check):
    check_first[i] = True
    check_second[i - check + N - 1] = True
    check_third[i + check] = True

    nqueen(check + 1)

    check_first[i] = False
    check_second[i - check + N - 1] = False
    check_third[i + check] = False

def nqueen(check):
    global result

    if check == N:
        result += 1

        return

    for i in range(N):
        if check_first[i]:
            continue
        else:
            if check_second[i - check + N - 1] or check_third[i + check]:
                continue
            else:
                truefalse(i, check)

check_first = [False] * N
check_second = [False] * (N * 2 - 1)
check_third = [False] * (N * 2 - 1)

if N % 2 == 0:
    for i in range(N // 2):
        truefalse(i, 0)

    print(result * 2)
else:
    for i in range(N // 2):
        truefalse(i, 0)

    result *= 2

    truefalse(N // 2, 0)

    print(result)