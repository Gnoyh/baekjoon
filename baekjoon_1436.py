# https://www.acmicpc.net/problem/1436

import sys

N = int(sys.stdin.readline())

check_list = ["666"]
result_set = set()

check = N

while check > 0:
    for i in range(10):
        for j in check_list:
            result_set.add(str(i) + str(j))
            result_set.add(str(j) + str(i))

    check -= len(result_set)

    check_list = list(result_set)

result_set = sorted(set(map(int, result_set)))

print(list(result_set)[N - 1])