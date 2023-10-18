# https://www.acmicpc.net/problem/4779

from sys import stdin

result_list = ["-"] * 13

for i in range(1, 13):
    result_list[i] = result_list[i - 1] + " " * (3 ** (i - 1)) + result_list[i - 1]

while True:
    try:
        N = int(stdin.readline())

        print(result_list[N])

    except:
        break