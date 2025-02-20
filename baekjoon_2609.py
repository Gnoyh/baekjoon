# https://www.acmicpc.net/problem/2609

import sys

a, b = map(int, sys.stdin.readline().strip().split())

max_num = max(a, b)
min_num = min(a, b)

while min_num > 0:
    max_num, min_num = min_num, max_num % min_num
            
print(max_num)
print(a * b // max_num)