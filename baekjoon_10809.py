# https://www.acmicpc.net/problem/10809

import sys

result_list = [-1 for i in range(26)]

input_str = str(sys.stdin.readline().strip())

for i in range(len(input_str)):
    if result_list[ord(input_str[i]) - 97] == -1:
        result_list[ord(input_str[i]) - 97] = i

for i in range(len(result_list)):
    print(result_list[i], end=" ")