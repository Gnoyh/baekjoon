# https://www.acmicpc.net/problem/9017

import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    
    t_list = list(map(int, sys.stdin.readline().strip().split()))
    
    count_dict = dict()
    count_set = set()
    
    for i in range(n):
        check = t_list[i]
        
        count_dict[check] = count_dict.get(check, 0) + 1
        
        if count_dict[check] == 6:
            count_set.add(check)
            
            count_dict[check] = 0
    
    point_dict = {'0': 10000}
    five_dict = {'0': 10000}
    
    count = 1
        
    for i in range(n):
        check = t_list[i]
        
        if check in count_set:
            count_dict[check] += 1
            
            if count_dict[check] < 5:
                point_dict[check] = point_dict.get(check, 0) + count
            elif count_dict[check] == 5:
                five_dict[check] = count
                
            count += 1
            
    result = '0'
    
    for i in point_dict:
        if point_dict[result] > point_dict[i]:
            result = i
        elif point_dict[result] == point_dict[i]:
            if five_dict[result] > five_dict[i]:
                result = i
                    
    print(result)