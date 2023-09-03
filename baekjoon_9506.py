# https://www.acmicpc.net/problem/9506

n = int(input())

while n != -1:
    check_sum = 0
    check_str = "{} =".format(n)

    for i in range(1, n // 2 + 1):
        if n % i == 0:
            check_sum += i
            check_str += " {} +".format(i)

            if check_sum > n:
                break

    if check_sum == n:
        print(check_str[: len(check_str) - 2])
    else:
        print("%d is NOT perfect." %n)

    n = int(input())