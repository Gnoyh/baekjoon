# https://www.acmicpc.net/problem/1138

import sys

n = int(sys.stdin.readline().strip())

new_list = [100] * n
check_list = list(map(int, sys.stdin.readline().strip().split()))

for i in range(n):
    height = i + 1
    check = check_list[i]
    count = 0
    
    for j in range(n):
        if check == count and new_list[j] == 100:
            new_list[j] = height
            
            break
            
        if new_list[j] > height:
            count += 1
            
for i in range(n - 1):
    print(new_list[i], end=" ")
    
print(new_list[-1])