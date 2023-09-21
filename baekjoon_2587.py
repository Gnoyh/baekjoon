# https://www.acmicpc.net/problem/2587

import sys

input_list = []

for i in range(5):
    input_list.append(int(sys.stdin.readline()))

input_list.sort()

print(sum(input_list) // 5)
print(input_list[2])