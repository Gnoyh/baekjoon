# https://www.acmicpc.net/problem/2738

N, M = map(int, input().split())

first_list = [[] for i in range(N)]
second_list = [[] for i in range(N)]

for i in range(N):
    input_list = list(map(int, input().split()))

    first_list[i] = input_list

for i in range(N):
    input_list = list(map(int, input().split()))

    second_list[i] = input_list

for i in range(N):
    for j in range(M):
        print(first_list[i][j] + second_list[i][j], end=" ")

    print()