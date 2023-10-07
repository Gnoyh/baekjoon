# https://www.acmicpc.net/problem/26069

from sys import stdin

N = int(stdin.readline())

def chongchong():
    check_set = {"ChongChong"}

    for _ in range(N):
        input_str = stdin.readline().strip().split()

        if input_str[0] in check_set:
            check_set.add(input_str[1])
        elif input_str[1] in check_set:
            check_set.add(input_str[0])

    print(len(check_set))

chongchong()