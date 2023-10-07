# https://www.acmicpc.net/problem/25192

from sys import stdin

N = int(stdin.readline())

def gomgom():
    check_set = set()

    result = 0

    for i in range(N):
        input_str = stdin.readline().strip()

        if input_str == "ENTER":
            result += len(check_set)

            check_set = set()
        else:
            check_set.add(input_str)

    print(result + len(check_set))

gomgom()