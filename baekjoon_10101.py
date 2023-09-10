# https://www.acmicpc.net/problem/10101

import sys

check_list = []

for i in range(3):
    check_list.append(int(sys.stdin.readline()))

if sum(check_list) != 180:
    print("Error")
else:
    if len(set(check_list)) == 1:
        print("Equilateral")
    elif len(set(check_list)) == 2:
        print("Isosceles")
    else:
        print("Scalene")