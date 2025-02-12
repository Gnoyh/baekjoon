# https://www.acmicpc.net/problem/17413

import sys

s = str(sys.stdin.readline().strip())

check = 0
result = ""
change = ""

for i in s:
    if i == '<':
        result += change + i
        
        check = 1
    elif i == '>':
        result += i
        
        check = 0
        change = ""
    elif check == 1:
        result += i
    elif i == ' ':
        result += change + i
        
        change = ""
    else:
        change = i + change
        
if change != "":
    result += change
        
print(result)