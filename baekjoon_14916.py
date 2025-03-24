# https://www.acmicpc.net/problem/14916

import sys

n = int(sys.stdin.readline().strip())

result = n // 5

n %= 5

if n % 2 == 0:
    result += n // 2
    n %= 2
else:
    if result > 0:
        result -= 1
        n += 5
    
    result += n // 2
    n %= 2
    
if n == 0:
    print(result)
else:
    print(-1)