# https://www.acmicpc.net/problem/1522

import sys

s = list(str(sys.stdin.readline().strip())[:])

count_a = 0
b_list = [0] * (len(s) * 2)

for i, v in enumerate(s):
    if v == 'a':
        count_a += 1
    else:
        b_list[i] = 1
        b_list[len(s) + i] = 1
        
result = sum(b_list[: count_a])
check = result

for i in range(len(s)):
    check = check - b_list[i] + b_list[count_a + i]
    
    result = min(result, check)
    
print(result)