# https://www.acmicpc.net/problem/4134

from sys import stdin

count = int(stdin.readline())

def prime(n):
    if n <= 2:
        print(2)

        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5 + 1), 2):
        if n % i == 0:
            return False

    print(n)

    return True

for i in range(count):
    n = int(stdin.readline())

    while True:
        if prime(n):
            break

        n += 1