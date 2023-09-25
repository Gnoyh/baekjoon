# https://www.acmicpc.net/problem/11478

import sys

input_str = sys.stdin.readline().strip()

count = 0

for i in range(len(input_str)):
    check_set = set()

    for j in range(len(input_str) - i):
        check_set.add(input_str[j: i + j + 1])

    count += len(check_set)

print(count)