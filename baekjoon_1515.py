# https://www.acmicpc.net/problem/1515

import sys

num = str(sys.stdin.readline().strip())

n = 1
idx = 0
check = -1

while idx < len(num):
    str_n = str(n)[check + 1: ]
    check_n = str_n.find(num[idx])
    
    if check_n == -1:
        check = -1
        
        n += 1
    else:
        idx += 1
        check += check_n + 1
        
print(n)