# https://www.acmicpc.net/problem/18870

import sys

N = int(sys.stdin.readline())

input_list = list(map(int, sys.stdin.readline().split()))
check_list = sorted(set(input_list))

check_dic = {check_list[i]: i for i in range(len(check_list))}

for i in input_list:
    print(check_dic[i], end=" ")