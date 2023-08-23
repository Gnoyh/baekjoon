# https://www.acmicpc.net/problem/2566

check_list = [[] for i in range(9)]

max_int = 0
max_x = 0
max_y = 0

for i in range(9):
    input_list = list(map(int, input().split()))

    for j in range(9):
        if input_list[j] >= max_int:
            max_int = input_list[j]
            max_x = j + 1
            max_y = i + 1

print(max_int)
print(max_y, max_x)