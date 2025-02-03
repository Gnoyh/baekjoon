# https://www.acmicpc.net/problem/11053

n = int(input())
num_list = list(map(int, input().split()))

check_list = [1]

for i in range(1, n):
    num = 1
    
    for j in range(i):
        if num_list[i] > num_list[j]:
            num = max(num, check_list[j] + 1)
            
    check_list.append(num)
        
print(max(check_list))