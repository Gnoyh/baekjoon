# https://www.acmicpc.net/problem/14929

import sys

n = int(sys.stdin.readline().strip())

x_list = list(map(int, sys.stdin.readline().strip().split()))

result = 0
check_sum = sum(x_list)

for i in range(n):
    check_sum -= x_list[i]
    
    result += x_list[i] * check_sum
    
print(result)