# https://www.acmicpc.net/problem/11054

n = int(input())
num_list = list(map(int, input().split()))

check_list = [1] * n
reverse_list = [0] * n

for i in range(1, n):
    check_num = 1
    rev_num = 0
    
    for j in range(i):
        if num_list[i] > num_list[j]:
            check_num = max(check_num, check_list[j] + 1)
            
        if num_list[n - 1 - i] > num_list[n - 1 - j]:
            rev_num = max(rev_num, reverse_list[n - 1 - j] + 1)
            
    check_list[i] = check_num
    reverse_list[n - 1 - i] = rev_num
            
result = 0

for i in range(n):
    result = max(result, check_list[i] + reverse_list[i])
    
print(result)