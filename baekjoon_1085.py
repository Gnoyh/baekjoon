# https://www.acmicpc.net/problem/1085

x, y, w, h = map(int, input().split())

check_list = [0 - x, w - x, 0 - y, h - y]

result = 1001

for i in check_list:
    if abs(i) < result:
        result = abs(i)

print(result)