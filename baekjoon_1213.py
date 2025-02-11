# https://www.acmicpc.net/problem/1213

import sys

name = str(sys.stdin.readline().strip())

alpha_dict = dict()

for i in name:
    alpha_dict[i] = alpha_dict.get(i, 0) + 1
    
alpha_list = sorted(list(alpha_dict))

check = 0

start = ""
middle = ""
end = ""

for i in alpha_list:
    count = alpha_dict[i] // 2
    
    start += i * count
    end = i * count + end
    
    if alpha_dict[i] % 2 == 1:
        if check == 1:
            check += 1
            
            break
        else:
            check = 1
            
            middle = i
            
if check > 1:
    print("I'm Sorry Hansoo")
else:
    print(start + middle + end)