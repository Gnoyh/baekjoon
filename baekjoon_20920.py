# https://www.acmicpc.net/problem/20920

from sys import stdin

N, M = map(int, stdin.readline().split())

def eng_memo():
    input_dict = dict()
    result_list = list()

    for _ in range(N):
        input_str = stdin.readline().rstrip()

        if len(input_str) >= M:
            if input_str in input_dict:
                input_dict[input_str] += 1
            else:
                input_dict[input_str] = 1

    input_dict = sorted(input_dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    for i in input_dict:
        result_list.append(i[0])

    print("\n".join(result_list))

eng_memo()