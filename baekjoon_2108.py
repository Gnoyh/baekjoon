# https://www.acmicpc.net/problem/2108

from sys import stdin

N = int(stdin.readline())

def statistics():
    input_list = [int(stdin.readline()) for _ in range(N)]
    result_list = list()

    input_list.sort()

    result_list.append(str(round(sum(input_list) / N)))
    result_list.append(str(input_list[N // 2]))

    check_list = [0] * 8001

    for i in input_list:
        check_list[i + 4000] += 1

    max_int = max(check_list)
    check = 0
    result = 0

    for i in range(8001):
        if check_list[i] == max_int:
            check += 1
            result = i - 4000

        if check == 2:
            break

    result_list.append(str(result))
    result_list.append(str(input_list[-1] - input_list[0]))

    print("\n".join(result_list))

statistics()