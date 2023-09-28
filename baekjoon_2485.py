# https://www.acmicpc.net/problem/2485

from sys import stdin
from math import gcd

N = int(stdin.readline())

input_list = list(int(stdin.readline()) for i in range(N))
check_list = list(set(input_list[i + 1] - input_list[i] for i in range(N - 1)))

check = check_list[0]

for i in range(1, len(check_list)):
    check = gcd(check, check_list[i])

print(((input_list[-1] - input_list[0]) // check - N + 1))