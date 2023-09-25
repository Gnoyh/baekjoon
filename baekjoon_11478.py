# https://www.acmicpc.net/problem/11478

import sys

input_str = sys.stdin.readline().strip()

check_set = set()

for i in range(len(input_str)):
    for j in range(i + 1, len(input_str) + 1):
        check_set.add(input_str[i: j])

print(len(check_set))