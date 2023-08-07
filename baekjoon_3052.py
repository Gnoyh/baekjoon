# https://www.acmicpc.net/problem/3052

check_list = [0 for i in range(42)]

for i in range(10):
    n = int(input())

    check_list[n % 42] = 1

result = 0

for i in range(42):
    if check_list[i] == 1:
        result += 1

print(result)