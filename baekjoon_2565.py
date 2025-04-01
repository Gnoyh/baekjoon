# https://www.acmicpc.net/problem/2565

import sys

n = int(sys.stdin.readline().strip())

num_list = []
num_dict = dict()

for i in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    
    num_list.append(a)
    num_dict[a] = b
    
num_list.sort()

check_list = [1]

for i in range(1, n):
    num = 1
    
    for j in range(i):
        if num_dict[num_list[i]] > num_dict[num_list[j]]:
            num = max(num, check_list[j] + 1)
            
    check_list.append(num)
        
print(n - max(check_list))