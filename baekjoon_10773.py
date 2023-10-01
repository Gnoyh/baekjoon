# https://www.acmicpc.net/problem/10773

from sys import stdin

K = int(stdin.readline())

input_list = list()

def zero():
    for i in range(K):
        n = int(stdin.readline())

        if n == 0:
            input_list.pop()
        else:
            input_list.append(n)

    print(sum(input_list))

zero()