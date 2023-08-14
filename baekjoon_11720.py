# https://www.acmicpc.net/problem/11720

N = int(input())

input_str = input()

result_int = 0

for i in range(N):
    result_int += int(input_str[i])

print(result_int)