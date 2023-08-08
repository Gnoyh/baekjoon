# https://www.acmicpc.net/problem/10871

N, X = map(int, input().split())

input_list = list(map(int, input().split()))

for i in range(N):
    if input_list[i] < X:
        print(input_list[i], end=" ")