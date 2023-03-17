# https://www.acmicpc.net/problem/25304

price1 = int(input())
price2 = 0
num = int(input())

for i in range(num):
    a, b = map(int, input().split())

    price2 += a * b

if (price1 == price2):
    print("Yes")
else:
    print("No")