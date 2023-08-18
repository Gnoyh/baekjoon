# https://www.acmicpc.net/problem/10988

input_str = input()

result = 1

for i in range(len(input_str) // 2):
    if input_str[i] != input_str[len(input_str) - 1 - i]:
        result = 0

        break

print(result)