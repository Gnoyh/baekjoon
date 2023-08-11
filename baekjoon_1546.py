# https://www.acmicpc.net/problem/1546

N = int(input())

input_list = list(map(int, input().split()))

input_max = 0
input_sum = 0

for i in range(N):
    if input_list[i] > input_max:
        input_max = input_list[i]

for i in range(N):
    input_list[i] = input_list[i] * 100 / input_max

    input_sum += input_list[i]

print(input_sum / N)