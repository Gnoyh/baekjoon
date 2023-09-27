# https://www.acmicpc.net/problem/1934

import sys
import math

T = int(sys.stdin.readline())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())

    print(math.lcm(A, B))