# https://www.acmicpc.net/problem/10807

N = int(input())

input_list = list(map(int, input().split()))

v = int(input())

count = 0

for i in range(N):
    if input_list[i] == v:
        count += 1

print(count)