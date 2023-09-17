# https://www.acmicpc.net/problem/1157

import sys

input_str = sys.stdin.readline().strip().upper()

check_max = 0
result = ""

for i in set(input_str):
    if check_max == input_str.count(i):
        result = "?"
    elif check_max < input_str.count(i):
        check_max = input_str.count(i)
        result = i

print(result)