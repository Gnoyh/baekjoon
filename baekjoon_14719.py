# https://www.acmicpc.net/problem/14719

import sys

h, w = map(int, sys.stdin.readline().strip().split())

block_list = list(map(int, sys.stdin.readline().strip().split()))
sum_list = [0] * w

max_h = 0
max_idx = 0

for i in range(w):
    for j in range(i - 1, max_idx, -1):
        if block_list[i] <= block_list[j]:
            break
        
        check_h = min(block_list[i], max_h)
        
        sum_list[j] = max(sum_list[j], check_h - block_list[j])
        
    if max_h <= block_list[i]:
        max_h = block_list[i]
        max_idx = i
        
print(sum(sum_list))