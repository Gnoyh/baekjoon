# https://www.acmicpc.net/problem/13241

import sys

A, B = map(int, sys.stdin.readline().split())

if B > A:
    change = A
    A = B
    B = change

result_A = A
result_B = B

while B != 0:
    A, B = B, A % B

print(result_A * result_B // A)