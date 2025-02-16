# https://www.acmicpc.net/problem/21918

import sys

n, m = map(int, sys.stdin.readline().strip().split())

n_list = list(map(int, sys.stdin.readline().strip().split()))

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    
    if a == 1:
        n_list[b - 1] = c
    elif a == 2:
        for i in range(b - 1, c):
            n_list[i] = (n_list[i] + 1) % 2
    elif a == 3:
        for i in range(b - 1, c):
            n_list[i] = 0
    else:
        for i in range(b - 1, c):
            n_list[i] = 1
            
for i in range(n - 1):
    print(n_list[i], end=" ")
    
print(n_list[-1])