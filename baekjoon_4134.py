# https://www.acmicpc.net/problem/4134

from sys import stdin

count = int(stdin.readline())

for i in range(count):
    n = int(stdin.readline())

    while True:
        check = 0

        if n <= 2:
            print(2)

            break

        if n % 2 == 0:
            n += 1

            continue

        for j in range(3, int(n ** 0.5 + 1), 2):
            if n % j == 0:
                n += 1
                check = 1

                break

        if check == 0:
            print(n)

            break