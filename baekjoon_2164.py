# https://www.acmicpc.net/problem/2164

from sys import stdin

N = int(stdin.readline())

def card():
    if N < 3:
        print(N)
    else:
        check = 4

        while True:
            if N <= check:
                print((N - check // 2) * 2)

                break

            check *= 2

card()