# https://www.acmicpc.net/problem/2852

import sys

n = int(sys.stdin.readline().strip())

point = 0
time_list = [0, 0]

start = 0

for _ in range(n):
    score = sys.stdin.readline().strip().split()
    
    team = score[0]
    time = int(score[1][: 2]) * 60 + int(score[1][3: ])
    
    if point < 0:
        time_list[0] += time - start
    elif point > 0:
        time_list[1] += time - start
        
    start = time
    
    if team == '1':
        point -= 1
    else:
        point += 1
        
if point < 0:
    time_list[0] += 2880 - start
elif point > 0:
    time_list[1] += 2880 - start

for i in time_list:
    h = i // 60
    m = i % 60
    
    print(f"{h:02}:{m:02}")