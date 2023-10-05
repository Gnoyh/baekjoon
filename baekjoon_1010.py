# https://www.acmicpc.net/problem/1010

from sys import stdin
from math import comb

T = int(stdin.readline())

for _ in range(T):
    N, M = map(int, stdin.readline().split())

    print(comb(M, N))