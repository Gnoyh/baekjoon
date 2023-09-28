# https://www.acmicpc.net/problem/1929

from sys import stdin

M, N = map(int, stdin.readline().split())

def prime(n):
    if n == 1:
        return False

    if n == 2:
        print(2)

        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5 + 1), 2):
        if n % i == 0:
            return False

    print(n)

    return True

for i in range(M, N + 1):
    if prime(i):
        continue