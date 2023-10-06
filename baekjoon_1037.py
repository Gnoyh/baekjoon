# https://www.acmicpc.net/problem/1037

from sys import stdin

N = int(stdin.readline())

input_list = list(map(int, stdin.readline().split()))

print(min(input_list) * max(input_list))