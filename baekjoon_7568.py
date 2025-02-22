# https://www.acmicpc.net/problem/7568

import sys

n = int(sys.stdin.readline().strip())

wh_list = []
rank_list = [1] * n

for i in range(n):
    w, h = map(int, sys.stdin.readline().strip().split())
    
    for j in range(i):
        if w > wh_list[j][0] and h > wh_list[j][1]:
            rank_list[j] += 1
        elif w < wh_list[j][0] and h < wh_list[j][1]:
            rank_list[i] += 1
            
    wh_list.append((w, h))
            
for i in range(n - 1):
    print(rank_list[i], end=" ")
    
print(rank_list[-1])