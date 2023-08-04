# https://www.acmicpc.net/problem/2562

result_max = 0
result_num = 0

for i in range(9):
    n = int(input())

    if n > result_max:
        result_max = n
        result_num = i + 1

print(result_max)
print(result_num)