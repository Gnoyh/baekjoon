# https://www.acmicpc.net/problem/20291

import sys

n = int(sys.stdin.readline().strip())

ex_dict = dict()

for _ in range(n):
    f, ex = map(str, sys.stdin.readline().strip().split("."))
    
    ex_dict[ex] = ex_dict.get(ex, 0) + 1
    
for i in sorted(list(ex_dict)):
    print(i, ex_dict[i])