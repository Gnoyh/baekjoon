# https://www.acmicpc.net/problem/2581

M = int(input())
N = int(input())

result_sum = 0
result_min = 0

for i in range(M, N + 1):
    check = 0

    if i == 2:
        result_sum += 2
        result_min = 2
    elif i != 1 and i % 2 == 1:
        for j in range(3, i // 3 + 1, 2):
            if i % j == 0:
                check = 1

                break

        if check == 0:
            result_sum += i

            if result_min == 0:
                result_min = i

if result_sum != 0:
    print(result_sum)
    print(result_min)
else:
    print(-1)