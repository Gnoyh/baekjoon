# https://www.acmicpc.net/problem/10798

import sys

check_list = []

result_str = ""

for i in range(5):
    input_str = str(sys.stdin.readline().strip())

    check_list.append(input_str)

for i in range(15):
    for j in range(5):
        if len(check_list[j]) > i:
            result_str += check_list[j][i]

print(result_str)