# https://www.acmicpc.net/problem/5073

import sys

check_list = []

while True:
    check_list = list(map(int, sys.stdin.readline().split()))

    if sum(check_list) == 0:
        break

    if max(check_list) < sum(check_list) - max(check_list):
        if len(set(check_list)) == 1:
            print("Equilateral")
        elif len(set(check_list)) == 2:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")