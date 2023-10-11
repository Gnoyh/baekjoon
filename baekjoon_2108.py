# https://www.acmicpc.net/problem/2108

from sys import stdin
from collections import Counter

N = int(stdin.readline())

def statistics():
    input_list = list()
    result_list = list()

    for _ in range(N):
        input_list.append(int(stdin.readline()))

    input_list.sort()

    result_list.append(str(round(sum(input_list) / N)))
    result_list.append(str(input_list[(N - 1) // 2]))

    counter_list = Counter(input_list).most_common()
    check_list = list()

    check = counter_list[0][1]

    for i in counter_list:
        if i[1] == check:
            check_list.append(i[0])

    if len(check_list) == 1:
        result_list.append(str(check_list[0]))
    else:
        result_list.append(str(check_list[1]))

    result_list.append(str(input_list[-1] - input_list[0]))

    print("\n".join(result_list))

statistics()