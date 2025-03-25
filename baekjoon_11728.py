# https://www.acmicpc.net/problem/11728

import sys

n, m = map(int, sys.stdin.readline().strip().split())

a_list = list(map(int, sys.stdin.readline().strip().split()))
b_list = list(map(int, sys.stdin.readline().strip().split()))

i, j, count = 0, 0, 0

while count < n + m - 1:
    if i == n:
        print(b_list[j], end=" ")
        
        j += 1
    elif j == m:
        print(a_list[i], end=" ")
        
        i += 1
    elif a_list[i] <= b_list[j]:
        print(a_list[i], end=" ")
        
        i += 1
    else:
        print(b_list[j], end=" ")
        
        j += 1
        
    count += 1
        
if i == n:
    print(b_list[j])
else:
    print(a_list[i])