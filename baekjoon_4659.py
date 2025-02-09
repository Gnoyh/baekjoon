# https://www.acmicpc.net/problem/4659

import sys

while True:
    pwd = str(sys.stdin.readline().strip())
    
    if pwd == "end":
        break
    
    aeiou_set = {'a', 'e', 'i', 'o', 'u'}
    
    aeiou_check = 0
    aeiou_count = 0
    else_count = 0
    result = ""
    
    if pwd[0] in aeiou_set:
        aeiou_check = 1
        
        aeiou_count += 1
    else:
        else_count += 1
        
    before_alpha = pwd[0]
    
    for i in pwd[1: ]:
        if before_alpha == i and i not in {'e', 'o'}:
            result = "not "
            
            break
        
        if i in aeiou_set:
            if aeiou_count == 0:
                aeiou_check = 1
                else_count = 0
                
            aeiou_count += 1
        else:
            if else_count == 0:
                aeiou_count = 0
                
            else_count += 1
            
        if aeiou_count == 3 or else_count == 3:
            result = "not "
            
            break
        
        before_alpha = i
        
    if aeiou_check == 0:
        result = "not "
        
        
    print(f"<{pwd}> is {result}acceptable.")