# https://www.acmicpc.net/problem/14467

import sys

n = int(sys.stdin.readline().strip())

cow_dict = dict()
count = 0

for _ in range(n):
    cow, road = map(int, sys.stdin.readline().strip().split())
    
    if cow_dict.get(cow, -1) == -1:
        cow_dict[cow] = road
    else:
        if cow_dict[cow] != road:
            count += 1
            
            cow_dict[cow] = road
            
print(count)