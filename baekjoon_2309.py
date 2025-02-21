# https://www.acmicpc.net/problem/2309

import sys

all_list = []

for _ in range(9):
    all_list.append(int(sys.stdin.readline().strip()))
    
sum_all = sum(all_list)

all_list.sort()

a, b = 0, 0

for i in range(8):
    check = 1
    
    for j in range(i + 1, 9):
        if all_list[i] + all_list[j] == sum_all - 100:
            a, b = i, j
            check = 0
            
            break
        
    if check == 0:
        break

for i in range(9):
    if i != a and i != b:
        print(all_list[i])