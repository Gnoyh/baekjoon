# https://www.acmicpc.net/problem/25501

from sys import stdin

T = int(stdin.readline())

def recursion():
    for _ in range(T):
        input_str = stdin.readline().rstrip()

        result = 0
        check = 0

        for i in range(len(input_str)):
            check += 1

            if i >= len(input_str) - i - 1:
                result = 1

                break
            elif input_str[i] != input_str[len(input_str) - i - 1]:
                result = 0

                break

        print(result, check)

recursion()