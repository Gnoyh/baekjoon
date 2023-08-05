# https://www.acmicpc.net/problem/10810

N, M = map(int, input().split())

result_list = [0 for i in range(N)]

for x in range(M):
    i, j, k = map(int, input().split())

    for y in range(i, j + 1):
        result_list[y - 1] = k

for i in range(N):
    if i == N - 1:
        print(result_list[i])
    else:
        print(result_list[i], end=" ")