# https://www.acmicpc.net/problem/1904

n = int(input())

a = 1
b = 1
result = 1

for i in range(2, n + 1):
    result = (a + b) % 15746
    
    a = b
    b = result
    
print(result)