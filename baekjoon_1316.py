# https://www.acmicpc.net/problem/1316

import sys

N = int(sys.stdin.readline().strip())

result = 0

for i in range(N):
    check_list = []
    check_str = ""
    check_int = 1

    input_str = sys.stdin.readline().strip()

    for j in input_str:
        if check_str == j:
            continue

        if j in check_list:
            check_int = 0

            break
        else:
            check_list.append(j)

        check_str = j

    if check_int == 1:
        result += 1

print(result)