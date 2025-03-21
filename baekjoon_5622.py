# https://www.acmicpc.net/problem/5622

import sys

check_list = []

for i in range(3, 11):
    if i == 8 or i == 10:
        for j in range(4):
            check_list.append(i)
    else:
        for j in range(3):
            check_list.append(i)

input_str = sys.stdin.readline().strip()

result_int = 0

for i in input_str:
    result_int += check_list[ord(i) - 65]

print(result_int)