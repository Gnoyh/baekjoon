# https://www.acmicpc.net/problem/20546

import sys

money = int(sys.stdin.readline().strip())

stock = list(map(int, sys.stdin.readline().strip().split()))

j_money = money % stock[0]
j_count = money // stock[0]

s_money = money
s_count = 0

check = 0

for i in range(1, len(stock)):
    if stock[i - 1] < stock[i]:
        if check < 0:
            check = 1
        else:
            check += 1
    elif stock[i - 1] > stock[i]:
        if check > 0:
            check = -1
        else:
            check -= 1
    else:
        check = 0
        
    if check >= 3 and s_count > 0:
        s_money = s_count * stock[i]
        s_count = 0
    elif check <= -3:
        s_count += s_money // stock[i]
        s_money = s_money % stock[i]
    
    j_count += j_money // stock[i]
    j_money = j_money % stock[i]

j_money = stock[-1] * j_count + j_money
s_money = stock[-1] * s_count + s_money

if j_money > s_money:
    print("BNP")
elif j_money == s_money:
    print("SAMESAME")
else:
    print("TIMING")