# https://www.acmicpc.net/problem/2869

import math

A, B, V = map(int, input().split())

V -= A

result = math.ceil(V / (A - B))

print(result + 1)