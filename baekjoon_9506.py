# https://www.acmicpc.net/problem/9506

import sys

while True:
    n = int(sys.stdin.readline().strip())

    if n == -1:
        break

    check_sum = 0
    check_str = "{} =".format(n)

    for i in range(1, n // 2 + 1):
        if n % i == 0:
            check_sum += i
            check_str += " {} +".format(i)

            if check_sum > n:
                break

    if check_sum == n:
        print(check_str[: -2])
    else:
        print("{} is NOT perfect.".format(n))