# https://www.acmicpc.net/problem/1735

import sys
import math

A1, B1 = map(int, sys.stdin.readline().split())
A2, B2 = map(int, sys.stdin.readline().split())

A, B = A1 * B2 + A2 * B1, B1 * B2

check = math.gcd(A, B)

print(A // check, B // check)