# https://www.acmicpc.net/problem/1343

import sys

board = sys.stdin.readline().strip() + "."

result = ""
count = 0

for i in board:
    if i == "X":
        count += 1
    elif i == "." and count != 0:
        if count % 2 == 1:
            result = -1
            
            break
        else:
            a = count // 4
            
            result += "AAAA" * a
            
            if count % 4 == 2:
                result += "BB"
                
            result += "."
            
        count = 0
    else:
        result += "."
        
if result == -1:
    print(result)
else:
    print(result[: -1])