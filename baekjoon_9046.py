# https://www.acmicpc.net/problem/9046

import sys

t = int(sys.stdin.readline())

str_list = []

for i in range(t):
    str_list.append(str(sys.stdin.readline().strip().replace(" ", "")))
    
    alpa_dict = dict()
    
    for j in str_list[i]:
        alpa_dict[j] = alpa_dict.get(j, 0) + 1
        
    max_num = 0
    count = 0
    result = ""
            
    for j in alpa_dict:
        if max_num == alpa_dict[j]:
            count += 1
        elif max_num < alpa_dict[j]:
            max_num = alpa_dict[j]
            count = 1
            result = j
            
    if count > 1:
        print("?")
    else:
        print(result)