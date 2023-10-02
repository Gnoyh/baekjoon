# https://www.acmicpc.net/problem/12789

from sys import stdin

N = int(stdin.readline())

input_list = list(map(int, stdin.readline().split()))

def snack_line():
    check_list = list()

    result = "Nice"

    check = 0
    count = 1

    while check < N:
        if input_list[check] == count:
            count += 1
            check += 1
        elif check_list and count == check_list[-1]:
            count += 1

            check_list.pop()
        elif check_list and input_list[check] < check_list[-1]:
            check_list.append(input_list[check])

            check += 1
        elif not check_list:
            check_list.append(input_list[check])

            check += 1
        else:
            result = "Sad"

            break

    return result

print(snack_line())