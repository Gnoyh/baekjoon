# https://www.acmicpc.net/problem/3009

result_x = 0
result_y = 0

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if x1 == x2:
    result_x = x3
else:
    if x1 == x3:
        result_x = x2
    else:
        result_x = x1

if y1 == y2:
    result_y = y3
else:
    if y1 == y3:
        result_y = y2
    else:
        result_y = y1

print(result_x, result_y)