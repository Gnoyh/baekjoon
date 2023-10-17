# https://www.acmicpc.net/problem/4779

from sys import stdin

def cantorian(N, str):
    if N == 0:
        str += "-"
    else:
        str = cantorian(N - 1, str)

        str += " " * (3 ** (N - 1))

        str = cantorian(N - 1, str)

    return str

while True:
    try:
        N = int(stdin.readline())

        result_str = ""

        print(cantorian(N, result_str))
    except:
        break