# https://www.acmicpc.net/problem/14888

from sys import stdin

N = int(stdin.readline())

input_list = list(map(int, stdin.readline().split()))

plus, minus, times, divide = map(int, stdin.readline().split())

max_int = -100 ** 11 - 1
min_int = 100 ** 11 + 1

def operator(result, check, plus, minus, times, divide):
    global max_int
    global min_int

    if check == N:
        if result > max_int:
            max_int = result

        if result < min_int:
            min_int = result

        return

    if plus > 0:
        operator(result + input_list[check], check + 1, plus - 1, minus, times, divide)

    if minus > 0:
        operator(result - input_list[check], check + 1,plus, minus - 1, times, divide)

    if times > 0:
        operator(result * input_list[check], check + 1, plus, minus, times - 1, divide)

    if divide > 0:
        if result < 0 or input_list[check] < 0:
            operator(-(abs(result) // abs(input_list[check])), check + 1, plus, minus, times, divide - 1)
        else:
            operator(abs(result) // abs(input_list[check]), check + 1, plus, minus, times, divide - 1)

operator(input_list[0], 1, plus, minus, times, divide)

print(max_int)
print(min_int)