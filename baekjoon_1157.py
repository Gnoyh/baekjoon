# https://www.acmicpc.net/problem/1157

import sys

input_str = sys.stdin.readline().strip().upper()

input_list = list(set(input_str))
check_list = []

for i in input_list:
    check_list.append(input_str.count(i))

if check_list.count(max(check_list)) > 1:
    print("?")
else:
    print(input_list[check_list.index(max(check_list))])