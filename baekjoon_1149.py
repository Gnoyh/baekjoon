# https://www.acmicpc.net/problem/1149

n = int(input())
color_list = []

for _ in range(n):
    color_list.append(list(map(int, input().split())))
    
cost_list = [[0, 0, 0] for _ in range(n)]

for i in range(3):
    cost_list[0][i] = color_list[0][i]
    
for i in range(1, n):
    cost_list[i][0] = color_list[i][0] + min(cost_list[i - 1][1], cost_list[i - 1][2])
    cost_list[i][1] = color_list[i][1] + min(cost_list[i - 1][0], cost_list[i - 1][2])
    cost_list[i][2] = color_list[i][2] + min(cost_list[i - 1][0], cost_list[i - 1][1])
    
print(min(cost_list[n - 1][0], cost_list[n - 1][1], cost_list[n - 1][2]))