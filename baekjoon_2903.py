# https://www.acmicpc.net/problem/2903

N = int(input())

result = 2

for i in range(N):
    result = result + result - 1

print(result ** 2)