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

input_list = sorted(list(input_set), reverse=True)

print("\n".join(input_list))