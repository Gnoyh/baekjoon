# https://www.acmicpc.net/problem/3003

check_list = [1, 1, 2, 2, 2, 8]

input_list = list(map(int, input().split()))

for i in range(6):
    print(check_list[i] - input_list[i], end=" ")