# https://www.acmicpc.net/problem/10870

from sys import stdin

n = int(stdin.readline())

def fibonacci():
    result_list = [0, 1]

    for i in range(2, n + 1):
        result_list.append(result_list[i - 2] + result_list[i - 1])

    print(result_list[n])

fibonacci()