# https://www.acmicpc.net/problem/28278

from sys import stdin

N = int(stdin.readline())

input_list = list()

for i in range(N):
    input_str = stdin.readline()

    if "1" in input_str:
        a, b = map(int, input_str.strip().split())

        input_list.append(b)
    elif "2" in input_str:
        if len(input_list) == 0:
            print(-1)
        else:
            a = input_list.pop()

            print(a)
    elif "3" in input_str:
        print(len(input_list))
    elif "4" in input_str:
        if len(input_list) == 0:
            print(1)
        else:
            print(0)
    elif "5" in input_str:
        if len(input_list) == 0:
            print(-1)
        else:
            print(input_list[-1])

