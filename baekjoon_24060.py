# https://www.acmicpc.net/problem/24060

from sys import stdin

N, K = map(int, stdin.readline().split())

input_list = list(map(int, stdin.readline().split()))

def merge_sort():
    check_list = []

    if N % 2 == 0:
        left_list = merge(N // 2, 0, check_list)
        right_list = merge(N // 2, N // 2, check_list)
    else:
        left_list = merge(N // 2 + 1, 0, check_list)
        right_list = merge(N // 2, N // 2 + 1, check_list)

    check_list.append([N, 0])

    check = 0

    for i in check_list:
        if check + i[0] >= K:
            check = K - check

            result_list = input_list[i[1]: i[0] + i[1]]
            result_list.sort()

            print(result_list[check - 1])

            break
        else:
            check += i[0]
    else:
        print(-1)

def merge(i, check, check_list):
    if i == 1:
        return [0, check, check_list]
    elif i == 2:
        check_list.append([2, check])

        return [2, check, check_list]
    else:
        if i % 2 == 0:
            left_list = merge(i // 2, check, check_list)
            right_list = merge(i // 2, check + left_list[0], check_list)
        else:
            left_list = merge(i // 2 + 1, check, check_list)
            right_list = merge(i // 2, check + left_list[0], check_list)

        check_list.append([i, check])

        return [i, check]

merge_sort()