# https://www.acmicpc.net/problem/25305

import sys

N, k = map(int, sys.stdin.readline().split())

input_list = list(map(int, sys.stdin.readline().split()))

input_list.sort(reverse=True)

print(input_list[k - 1])