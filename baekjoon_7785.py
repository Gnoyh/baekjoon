# https://www.acmicpc.net/problem/7785

import sys

n = int(sys.stdin.readline())

input_set = set()

for i in range(n):
    a, b = sys.stdin.readline().strip().split()

    if b == "enter":
        input_set.add(a)
    else:
        input_set.remove(a)

for i in sorted(input_set, reverse=True):
    print(i)