# https://www.acmicpc.net/problem/1932

n = int(input())
tri_list = [list(map(int, input().split())) for _ in range(n)]
sum_list = [[0 for _ in range(i)] for i in range(1, n + 1)]

sum_list[0][0] = tri_list[0][0]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            sum_list[i][j] = tri_list[i][j]+ sum_list[i - 1][j]
        elif j == i:
            sum_list[i][j] = tri_list[i][j] + sum_list[i - 1][j - 1]
        else:
            sum_list[i][j] = tri_list[i][j] + max(sum_list[i - 1][j - 1], sum_list[i - 1][j])
            
print(max(sum_list[n - 1]))