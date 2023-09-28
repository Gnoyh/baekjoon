# https://www.acmicpc.net/problem/2485

from sys import stdin
from math import gcd

N = int(stdin.readline())

input_list = list()

for i in range(N):
    input_list.append(int(stdin.readline()))

input_list.sort()

check_list = list()

for i in range(len(input_list) - 1):
    check_list.append(input_list[i + 1] - input_list[i])

check = check_list[0]

for i in range(1, len(check_list)):
    check = gcd(check, check_list[i])

print((max(input_list) - min(input_list)) // check - len(input_list) + 1)