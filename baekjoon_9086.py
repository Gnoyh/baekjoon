# https://www.acmicpc.net/problem/9086

T = int(input())

for i in range(T):
    input_str = input()

    print(input_str[0] + input_str[len(input_str) - 1])