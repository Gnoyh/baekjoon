# https://www.acmicpc.net/problem/27433

from sys import stdin

N = int(stdin.readline())

result = 1

for i in range(1, N + 1):
    result *= i

print(result)