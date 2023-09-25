# https://www.acmicpc.net/problem/11478

import sys

input_str = sys.stdin.readline().strip()

check_list = []

for i in range(len(input_str) + 1):
    for j in range(i + 1, len(input_str) + 1):
        check_list.append(input_str[i: j])

print(len(set(check_list)))