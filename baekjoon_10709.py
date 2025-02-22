# https://www.acmicpc.net/problem/10709

import sys

h, w = map(int, sys.stdin.readline().strip().split())

for _ in range(h):
    w_list = list(str(sys.stdin.readline().strip()))
    check = -1
    result = ""
    
    for j in w_list:
        if j == "c":
            check = 0
        elif check != -1:
            check += 1
        
        result += f" {check}"
        
    print(result[1: ])