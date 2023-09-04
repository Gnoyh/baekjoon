# https://www.acmicpc.net/problem/1978

N = int(input())

input_list = list(map(int, input().split()))

result = 0

for i in input_list:
    check = 0

    if i == 2:
        result += 1
    elif i != 1 and i % 2 == 1:
        for j in range(3, i // 2 + 1):
            if i % j == 0:
                check = 1

                break

        if check == 0:
            result += 1

print(result)