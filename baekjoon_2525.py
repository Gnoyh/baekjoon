# https://www.acmicpc.net/problem/2525

h, m = map(int, input().split())
num = int(input())

if (m + num >= 60):
    h += (m + num) // 60
    m = (m + num) % 60

    if (h >= 24):
        h %= 24
else:
    m = m + num

print(h, m)