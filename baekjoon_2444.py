# https://www.acmicpc.net/problem/2444

N = int(input())

for i in range(1, N * 2):
    check = abs(N - i)

    print(" " * check + "*" * ((N * 2 - 1) - (check * 2)))