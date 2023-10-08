# https://www.acmicpc.net/problem/20920

from sys import stdin
from collections import Counter

N, M = map(int, stdin.readline().split())

def eng_memo():
    input_list = list()

    for _ in range(N):
        input_str = stdin.readline().rstrip()

        if len(input_str) >= M:
            input_list.append(input_str)

    input_count = Counter(input_list)

    input_list = sorted(input_count)
    input_list = sorted(input_list, key=len, reverse=True)
    input_list = sorted(input_list, key=input_count.get, reverse=True)

    print("\n".join(input_list))

eng_memo()