# https://www.acmicpc.net/problem/2588

num1 = int(input())
num2 = int(input())

result = num1 * num2

for i in range(3):
    print(num1 * (num2 % 10))

    num2 = num2 // 10

print(result)



