# https://www.acmicpc.net/problem/5618

import sys

n = int(sys.stdin.readline().strip())

num_list = list(map(int, sys.stdin.readline().strip().split()))

num_list.sort(reverse = True)

check_list = []

for i in range(1, int(num_list[-1] ** (0.5)) + 1):
    if num_list[-1] % i == 0:
        check_list.append(i)
        check_list.append(num_list[-1] // i)
        
check_list = sorted(list(set(check_list)))

num_list.pop()
        
for i in check_list:
    check = 1
    
    for j in num_list:
        if j % i != 0:
            check = 0
            
            break
        
    if check == 1:
        print(i)