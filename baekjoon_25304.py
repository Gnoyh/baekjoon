# https://www.acmicpc.net/problem/25304

import sys

price1 = int(sys.stdin.readline().strip())
price2 = 0
num = int(sys.stdin.readline().strip())

for i in range(num):
    a, b = map(int, sys.stdin.readline().strip().split())

    price2 += a * b

if (price1 == price2):
    print("Yes")
else:
    print("No")