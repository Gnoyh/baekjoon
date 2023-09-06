# https://www.acmicpc.net/problem/1978

N = int(input())

input_list = list(map(int, input().split()))

check_list = [1 for i in range(max(input_list) + 1)]

check_list[0] = 0
check_list[1] = 0

result = 0

for i in range(4, max(input_list) + 1, 2):
    check_list[i] = 0

for i in range(3, int(max(input_list) ** 0.5) + 1, 2):
    if check_list[i] == 1:
        for j in range(i * 3, max(input_list) + 1, i):
            check_list[j] = 0

for i in input_list:
    if check_list[i] == 1:
        result += 1

print(result)