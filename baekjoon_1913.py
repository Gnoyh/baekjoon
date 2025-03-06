# https://www.acmicpc.net/problem/1913

import sys

n = int(sys.stdin.readline().strip())
find = int(sys.stdin.readline().strip())

graph = [[0] * (n + 1) for _ in range(n + 1)]
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

point = (n // 2 + 1, n // 2 + 1)
find_point = (0, 0)

check = 1
count = 1
move_idx = 0

while count <= n ** 2:
    graph[point[0]][point[1]] = count
    
    if find == count:
        find_point = (point[0], point[1])
    
    if count == check ** 2:
        check += 2
    
    count += 1
    
    limit_min = n // 2 + 1 - (check // 2)
    limit_max = n // 2 + 1 + (check // 2)
    
    if move_idx in (0, 2) and limit_min <= point[0] + move[move_idx][0] <= limit_max:
        pass
    elif move_idx in (1, 3) and limit_min <= point[1] + move[move_idx][1] <= limit_max:
        pass
    else:
        move_idx = (move_idx + 1) % 4
        
    point = (point[0] + move[move_idx][0], point[1] + move[move_idx][1])
            
for i in range(1, n + 1):
    for j in range(1, n):
        print(graph[i][j], end=" ")
        
    print(graph[i][n])
    
print(find_point[0], find_point[1])