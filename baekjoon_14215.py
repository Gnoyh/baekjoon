# https://www.acmicpc.net/problem/14215

import sys

check_list = list(map(int, sys.stdin.readline().split()))
check_int = sum(check_list) - max(check_list)

if max(check_list) < check_int:
    print(sum(check_list))
else:
    print(check_int * 2 - 1)