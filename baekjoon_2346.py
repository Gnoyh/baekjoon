# https://www.acmicpc.net/problem/2346

from sys import stdin

N = int(stdin.readline())

input_list = list(map(int, stdin.readline().split()))

def balloon():
    check_list = list((str(i + 1) + " " + str(input_list[i]) for i in range(N)))
    result_list = list()

    check = 0

    while True:
        check_str = check_list.pop(check).split()

        result_list.append(check_str[0])

        if not check_list:
            break

        if int(check_str[1]) < 0:
            check = (check + int(check_str[1])) % len(check_list)
        else:
            check = (check + int(check_str[1]) - 1) % len(check_list)

    print(" ".join(result_list))

balloon()