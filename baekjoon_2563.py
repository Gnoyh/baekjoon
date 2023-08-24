# https://www.acmicpc.net/problem/2563

N = int(input())

check_list = [[0 for i in range(100)] for j in range(100)]

result = 0

for i in range(N):
    a, b = map(int, input().split())

    for j in range(a, a + 10):
        for k in range(b, b + 10):
            if check_list[j][k] == 0:
                check_list[j][k] = 1
                result += 1

print(result)